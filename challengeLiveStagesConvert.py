import os
import json
from collections import OrderedDict

# Helper function to generate rank name in correct format
def rank_to_name(rank):
    if rank % 10 == 1 and rank != 11:
        return f"{rank}st"
    elif rank % 10 == 2 and rank != 12:
        return f"{rank}nd"
    elif rank % 10 == 3 and rank != 13:
        return f"{rank}rd"
    else:
        return f"{rank}th"

def convert_challenge_live_stages(input_dir, output_dir):
    # 构建输入文件和输出文件的完整路径
    input_file = os.path.join(input_dir, 'challengeLiveStages.json')
    output_file = os.path.join(output_dir, 'challengeLiveStages.json')

    # 打开并读取输入文件
    with open(input_file, 'r', encoding='utf-8') as f:
        action_sets = json.load(f)

    # 定义字段映射列表，包含每个字段在原数组中的索引和目标字段名
    fields = [
        (0, "id"),  # 动态生成
        (1, "characterId"),  # 来自原数据
        (2, "rank"),  # 来自原数据
        (3, "name"),  # 动态生成
        (4, "nextStageChallengePoint"),  # 来自原数据
        (5, "completeStageResourceBoxId"),  # 固定为1
        (6, "completeStageCharacterExp"),  # 固定为1
    ]

    # 转换后的结果列表
    converted_action_sets = []

    # 遍历每个元素并进行转换，索引从 0 开始
    for idx, item in enumerate(action_sets):
        # 使用 OrderedDict 确保字段的顺序一致
        converted_item = OrderedDict()

        # 动态生成的字段
        generated_data = {
            "id": idx + 1,  # 序号从1开始生成
            "name": rank_to_name(item[1]),  # 生成rank的字符串表达
            "completeStageResourceBoxId": 1,  # 固定为1
            "completeStageCharacterExp": 1  # 固定为1
        }

        # 从输入数据中提取的字段
        character_id, rank, next_stage_challenge_point = item[0], item[1], item[2]

        # 遍历字段映射并填充数据
        for index, field_name in fields:
            if field_name in generated_data:
                # 如果字段是动态生成的，使用生成的数据
                converted_item[field_name] = generated_data[field_name]
            else:
                # 根据映射的字段名称填充相应的数据
                if field_name == "characterId":
                    converted_item[field_name] = character_id
                elif field_name == "rank":
                    converted_item[field_name] = rank
                elif field_name == "nextStageChallengePoint":
                    converted_item[field_name] = next_stage_challenge_point

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
    convert_challenge_live_stages(input_directory, output_directory)
