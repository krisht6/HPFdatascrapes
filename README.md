# HPFdatascrapes

HPF: Hyper-Palatable Foods
The raw data is protected by the University at Buffalo Department of Behavioral Medicine. 
Attached are the 3 python scripts used to scrape, clean, and group the data as needed.

The first file, [filterliquidsnew.csv] was used to remove any liquid entries from the data set as per the "Protocol for Determination of Hyper-palatable Foods: Steps for Processing Nutrient Data and Applying Hyper-Palatable Food Definition" by Dr. Fazzino.

Second, the file [newgrouping.py] was used to group entries together.

We implemented a custom grouping logic based on the 'FoodNum' and 'FoodType' columns.
Food items were grouped together if they shared the same 'FoodNum'
Additionally, if a food item had a 'FoodType' of 2, it was grouped with the preceding item, thereby linking certain items based on their sequence and type.

Within each group:
For the 'Food_Description' column the script concatenated text descriptions for items within the same group, creating a comprehensive description for grouped foods.
Kept the columns discussed that we needed for further scoring ('UserName', 'RecallNo', 'IntakeDate', 'Occ_Time', 'Occ_Name', 'FoodCode').
For nutritional content columns (from the 25th to the 91st column), the script summed up the values to provide aggregated nutritional data for each group.

Finally, the file, [remove0cal.py] wasused to remove any grouped entries that had 0 KCAL as a calculation of percent calories from fat, sugar, or carbohydrates is not possible with zero calories

