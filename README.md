# sekai-master-db-tc-to-std

Python scripts for aligning the Project Sekai (Traditional Chinese) Master DB to Project Sekai (Japanese) Master DB

Build for Project Sekai (Traditional Chinese) Master DB **version 3.4.0**.

**This repository is not fully functional yet. The script is still under development.**

## Usage

1. Clone this repository
```bash
git clone https://github.com/Zeric-li/sekai-master-db-tc-to-std.git
```
2. Navigate to the cloned repository
```bash
cd sekai-master-db-tc-to-std
```
3. Clone the Project Sekai (Traditional Chinese) Master DB from [Sekai-World/sekai-master-db-tc-diff](https://github.com/Sekai-World/sekai-master-db-tc-diff)
```bash 
git clone https://github.com/Sekai-World/sekai-master-db-tc-diff.git
```
4. Clone the Project Sekai (Japanese) Master DB from [Sekai-World/sekai-master-db-diff](https://github.com/Sekai-World/sekai-master-db-diff)
```bash 
git clone https://github.com/Sekai-World/sekai-master-db-diff.git
```
5. Run the script with the following command:
```bash
python start.py
```
6. The script will generate the aligned new DB named `sekai-master-db-tc-to-std` in the same directory
   - Notice that since the full conversion scripts are not implemented yet, the script will only align the files that are already implemented.

## Status

- [x] actionSets.json
- [x] areaItemLevels.json
- [x] billingShopItems.json
- [x] bondsHonors.json
- [x] cardCostume3ds.json
- [x] cards.json
- [x] challengeLiveHighScoreRewards.json
- [x] challengeLiveStageExs.json
- [x] challengeLiveStages.json
- [ ] Other files (about 25 more files needs to be aligned)
