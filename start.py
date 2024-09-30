import os
import actionSetsConvert
import areaItemLevelsConvert
import billingShopItemsConvert
import bondsHonorsConvert
import cardCostume3dsConvert
import cardsConvert
import challengeLiveHighScoreRewardsConvert
import challengeLiveStagesConvert

if __name__ == "__main__":
    # 指定输入文件夹和输出文件夹路径
    input_folder = './sekai-master-db-tc-diff'
    output_folder = './sekai-master-db-tc-std-diff'

    # 确保输入文件夹存在
    if not os.path.exists(input_folder):
        print(f"Error: Input folder {input_folder} does not exist.")
    else:
        # 调用转换函数
        actionSetsConvert.convert_action_sets(input_folder, output_folder)
        print(f"Conversion complete. Output saved to {output_folder}/actionSets.json")
        areaItemLevelsConvert.convert_area_item_levels(input_folder, output_folder)
        print(f"Conversion complete. Output saved to {output_folder}/areaItemLevels.json")
        billingShopItemsConvert.convert_billing_shop_items(input_folder, output_folder)
        print(f"Conversion complete. Output saved to {output_folder}/billingShopItems.json")
        bondsHonorsConvert.convert_bonds_honors(input_folder, output_folder)
        print(f"Conversion complete. Output saved to {output_folder}/bondsHonors.json")
        cardCostume3dsConvert.convert_card_costume_3ds(input_folder, output_folder)
        print(f"Conversion complete. Output saved to {output_folder}/cardCostume3ds.json")
        cardsConvert.convert_cards(input_folder, output_folder)
        print(f"Conversion complete. Output saved to {output_folder}/cards.json")
        challengeLiveHighScoreRewardsConvert.convert_challenge_live_high_score_rewards(input_folder, output_folder)
        print(f"Conversion complete. Output saved to {output_folder}/challengeLiveHighScoreRewards.json")
        challengeLiveStagesConvert.convert_challenge_live_stages(input_folder, output_folder)
        print(f"Conversion complete. Output saved to {output_folder}/challengeLiveStages.json")
