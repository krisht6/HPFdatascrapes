# Hyper-Palatable Foods (HPF) Analysis  
**Data Processing for University at Buffalo Department of Behavioral Medicine**  

This repository contains three Python scripts used to scrape, clean, and group raw nutritional data for the analysis of Hyper-Palatable Foods (HPF), as defined by Dr. Fazzino’s *Protocol for Determination of Hyper-Palatable Foods*. The raw data is proprietary and protected by the University at Buffalo Department of Behavioral Medicine, so only the processing scripts are included here.  

## Scripts & Functionality  

### 1. `filterliquidsnew.csv`  
- **Purpose**: Removes liquid entries from the dataset.  
- **Details**: Follows the protocol by Dr. Fazzino to exclude liquids, ensuring only solid food items remain for HPF analysis.  

### 2. `newgrouping.py`  
- **Purpose**: Groups food entries based on custom logic for cohesive analysis.  
- **Grouping Logic**:  
  - Groups items with the same `FoodNum`.  
  - Links items with `FoodType = 2` to the preceding item, preserving sequence-based relationships.  
- **Processing**:  
  - **Food_Description**: Concatenates descriptions within each group for a unified text output.  
  - **Key Columns**: Retains essential columns (`UserName`, `RecallNo`, `IntakeDate`, `Occ_Time`, `Occ_Name`, `FoodCode`) for scoring.  
  - **Nutritional Data**: Sums values from columns 25 to 91 to aggregate nutritional content per group.  

### 3. `remove0cal.py`  
- **Purpose**: Filters out grouped entries with zero calories (KCAL).  
- **Details**: Removes entries where KCAL = 0, as percent calorie calculations (e.g., from fat, sugar, or carbohydrates) are undefined, ensuring data integrity for HPF scoring.  

## Tech Stack  
- Python  
- Pandas (assumed for CSV handling and data manipulation)  

## Notes  
- The raw data is not included due to university restrictions.  
- These scripts align with Dr. Fazzino’s HPF protocol for processing nutrient data and applying definitions.  
- Contributions or questions about the methodology are welcome, though data access is restricted.  

Explore the scripts to understand the data cleaning and grouping process for HPF research!  
