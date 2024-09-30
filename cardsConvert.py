import os
import json
from collections import OrderedDict


def convert_cards(input_dir, output_dir):
    # 构建输入文件和输出文件的完整路径
    input_file = os.path.join(input_dir, 'cards.json')
    output_file = os.path.join(output_dir, 'cards.json')

    # 打开并读取输入文件
    with open(input_file, 'r', encoding='utf-8') as f:
        action_sets = json.load(f)

    # 定义字段映射列表，确保没有重复字段
    fields = [
        (0, "id"),
        (1, "seq"),
        (2, "characterId"),
        (3, "cardRarityType"),
        (4, "specialTrainingPower1BonusFixed"),
        (5, "specialTrainingPower2BonusFixed"),
        (6, "specialTrainingPower3BonusFixed"),
        (7, "attr"),
        (8, "supportUnit"),
        (9, "skillId"),
        (10, "cardSkillName"),
        (11, "prefix"),
        (12, "assetbundleName"),
        (13, "gachaPhrase"),
        (14, "archiveDisplayType"),
        (15, "releaseAt"),
        (16, "cardParameters"), # 只提供了每组“param”下顺序排列的“power”数值，需要处理以还原为原始格式
        (17, "specialTrainingCosts"), # 需要处理以还原为原始格式
        (18, "masterLessonAchieveResources")  # 只提供了两个字段，姑且当做是"masterRank"和"resources", 需要处理以还原为原始格式
        # 忽略最后一个字段，疑似为"releaseAt"的重复
    ]

    # 转换后的结果列表
    converted_action_sets = []

    # 遍历每个元素并进行转换，丢弃最后的一个字段
    for item in action_sets:
        # 使用 OrderedDict 确保字段的顺序一致
        converted_item = OrderedDict()

        # 特殊处理 cardParameters 字段，确保它放在正确的顺序位置
        card_parameters = []
        if item[16]:  # index 16 是 cardParameters
            card_id = item[0]  # 获取卡片ID

            # 动态处理paramX字段，遍历item[16]中所有的键和值
            for param_type, param_values in item[16].items():
                # 获取 paramX 中的 X 值 (例如 "param1" 的 X 值是 1)
                param_x = int(param_type.replace("param", "")) - 1

                # 构建参数的ID
                for level, power in enumerate(param_values, 1):
                    # 三位从 001 开始的序号
                    sequence = f"{level:03d}"
                    # 生成ID: cardId + paramX的X值减一 + 序号
                    param_id = f"{card_id}{param_x}{sequence}"

                    # 添加到 card_parameters 列表
                    card_parameters.append({
                        "id": param_id,
                        "cardId": card_id,
                        "cardLevel": level,
                        "cardParameterType": param_type,  # 动态使用paramX作为类型
                        "power": power
                    })

        # 特殊处理 specialTrainingCosts 字段
        special_training_costs = []
        if item[17]:  # index 17 是 specialTrainingCosts
            card_id = item[0]  # 获取卡片ID
            for cost_item in item[17]:
                # 构造 specialTrainingCosts 的结构
                special_training_costs.append({
                    "cardId": card_id,
                    "seq": cost_item[1],
                    "cost": {
                        "resourceId": cost_item[2][0],
                        "resourceType": cost_item[2][1],
                        "resourceLevel": cost_item[2][2],
                        "quantity": cost_item[2][3]
                    }
                })

        # 特殊处理 masterLessonAchieveResources 字段
        master_lesson_achieve_resources = []
        if item[18]:  # index 18 是 masterLessonAchieveResources
            card_id = item[0]  # 获取卡片ID
            for resource in item[18]:
                # resource 是一个数组，第一个值是 masterRank，第二个值是 resources
                master_lesson_achieve_resources.append({
                    "cardId": card_id,
                    "masterRank": resource[0],
                    "resources": resource[1]
                })

        # 遍历字段映射，并按顺序插入
        for index, field_name in fields:
            if field_name == "cardParameters":
                # 在 index=16 位置插入 cardParameters
                converted_item[field_name] = card_parameters
            elif field_name == "specialTrainingCosts":
                # 在 index=17 位置插入 specialTrainingCosts
                converted_item[field_name] = special_training_costs
            elif field_name == "masterLessonAchieveResources":
                # 在 index=18 位置插入 masterLessonAchieveResources
                converted_item[field_name] = master_lesson_achieve_resources
            elif index < len(item) - 1 and item[index] is not None:  # 忽略最后一个字段
                converted_item[field_name] = item[index]

        # 添加转换后的对象到列表
        converted_action_sets.append(converted_item)

    # 确保输出文件夹存在
    os.makedirs(output_dir, exist_ok=True)

    # 将转换后的数据写入输出文件
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(converted_action_sets, f, ensure_ascii=False, indent=2)


# 如果直接运行此脚本，提供默认输入输出路径
if __name__ == "__main__":
    input_directory = './sekai-master-db-tc-diff'
    output_directory = './sekai-master-db-tc-std-diff'
    convert_cards(input_directory, output_directory)