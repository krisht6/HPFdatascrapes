import pandas as pd

# loading data
data = pd.read_csv('food codes.csv')

# keywords/exclusions
liquid_keywords = [
    "milk", "water", "tea", "soda", "juice", "infant formula", 
    "nutritional drink", "meal replacement", "coffee", "alcoholic", 
    "fluid replacement", "fruit nectar", "power mix", "hot chocolate", 
    "broth", "smoothie", "milkshake", "horchata", "orange julius", 
    "pina colada", "eggnog"
]
exclude_keywords = [
    "frozen", "ice cream", "yogurt", "cheese", "steak", "pork", 
    "beef", "chicken", "fish", "cookie", "cake", "bread", "pie", 
    "cereal bar", "nutrition bar", "cracker", "pastry"
]

# filitering function 
def is_liquid(description):
    desc_lower = description.lower()
    if any(exclude in desc_lower for exclude in exclude_keywords):
        return False  # exclude any edge case solids
    return any(word in desc_lower for word in liquid_keywords)

# filtering
liquids = data[data['Main food description'].apply(is_liquid)]

pd.set_option('display.max_rows', None)  # Display all rows
pd.set_option('display.max_columns', None)  # Display all columns (if necessary)


print(liquids[['Food code', 'Main food description']])




# liquids is the DF containing filtered liquids
liquid_food_codes = set(liquids['Food code'].unique())


# loading recall
recall_data = pd.read_csv('Habit_32815_INF.csv')

# covert the 'FoodCode' column to the same type as in the 'liquids' DF 
recall_data['FoodCode'] = recall_data['FoodCode'].astype(liquids['Food code'].dtype)

# filter out liquids
recall_data_filtered = recall_data[~recall_data['FoodCode'].isin(liquid_food_codes)]

# save the filtered recall data to a new csv file
recall_data_filtered.to_csv('filtered_recall_data.csv', index=False)


# filtering took out 11,000 lines of liquid recall data


