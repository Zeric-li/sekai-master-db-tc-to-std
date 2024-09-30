import os
import json
from collections import OrderedDict

def convert_billing_shop_items(input_dir, output_dir):
    # 构建输入文件和输出文件的完整路径
    input_file = os.path.join(input_dir, 'billingShopItems.json')
    output_file = os.path.join(output_dir, 'billingShopItems.json')

    # 打开并读取输入文件
    with open(input_file, 'r', encoding='utf-8') as f:
        action_sets = json.load(f)

    # 定义字段映射列表，包含每个字段在原数组中的索引和目标字段名
    fields = [
        (0, "id"),
        (1, "seq"),
        (2, "billingShopItemType"),
        (3, "billingProductGroupId"),
        (4, "saleType"),
        (5, "name"),
        (6, "description"),
        (7, "billableLimitType"),
        (8, "billableLimitValue"),
        (9, "billableLimitResetIntervalType"),
        (10, "billableLimitResetIntervalValue"),
        (11, "assetbundleName"),
        (12, "resourceBoxId"),
        (13, "bonusResourceBoxId"),
        (14, "label"),
        (15, "startAt"),
        (16, "endAt"),
        (17, "purchaseOption")
    ]

    # 转换后的结果列表
    converted_action_sets = []

    # 遍历每个元素并进行转换
    for item in action_sets:
        # 使用 OrderedDict 确保字段的顺序一致
        converted_item = OrderedDict()

        # 统一遍历字段映射列表，并按顺序检查是否为 None
        for index, field_name in fields:
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
    convert_billing_shop_items(input_directory, output_directory)
