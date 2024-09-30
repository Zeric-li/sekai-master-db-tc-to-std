import os
import json
from collections import OrderedDict

def convert_bonds_honors(input_dir, output_dir):
    # 构建输入文件和输出文件的完整路径
    input_file = os.path.join(input_dir, 'bondsHonors.json')
    output_file = os.path.join(output_dir, 'bondsHonors.json')

    # 打开并读取输入文件
    with open(input_file, 'r', encoding='utf-8') as f:
        action_sets = json.load(f)

    # 定义字段映射列表，包含每个字段在原数组中的索引和目标字段名
    fields = [
        (0, "id"),
        (1, "seq"),
        (2, "bondsGroupId"),
        (3, "gameCharacterUnitId1"),
        (4, "gameCharacterUnitId2"),
        (5, "honorRarity"),
        (6, "name"),
        (7, "description"),
        (8, "levels"),  # levels 将需要特殊处理
        (9, "configurableUnitVirtualSinger")
    ]

    # 转换后的结果列表
    converted_action_sets = []

    # 遍历每个元素并进行转换
    for item in action_sets:
        # 使用 OrderedDict 确保字段的顺序一致
        converted_item = OrderedDict()

        # 统一遍历字段映射列表，并按顺序检查是否为 None
        for index, field_name in fields:
            if field_name == "levels":
                # 处理 levels 的嵌套数组
                levels = item[index]
                converted_levels = []
                for level in levels:
                    converted_level = {
                        "id": level[0],
                        "bondsHonorId": level[1],
                        "level": level[2],
                        "description": level[3]
                    }
                    converted_levels.append(converted_level)
                converted_item["levels"] = converted_levels
            else:
                # 处理其他简单字段
                if item[index] is not None:
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
    convert_bonds_honors(input_directory, output_directory)
