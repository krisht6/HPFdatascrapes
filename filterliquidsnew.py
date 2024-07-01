import pandas as pd

# Load the data from the CSV file
file_path = 'Habit_updated.csv'
df = pd.read_csv(file_path)

# Keywords indicating a liquid
liquid_keywords = [
    "milk", "water", "tea", "soda", "juice", "infant formula",
    "nutritional drink", "meal replacement", "coffee", "alcoholic",
    "fluid replacement", "fruit nectar", "power mix", "hot chocolate",
    "broth", "smoothie", "milkshake", "horchata", "orange juice",
    "pina colada", "eggnog", "beer", "soft drink", "drink", "cocktail"
]

# Keywords to exclude from being considered liquids
exclude_keywords = [
    "frozen", "ice cream", "yogurt", "cheese", "steak", "pork",
    "beef", "chicken", "fish", "cookie", "cake", "bread", "pie",
    "cereal bar", "nutrition bar", "cracker", "pastry"
]

# Filtering function to determine if a description mentions a liquid
def is_liquid(description):
    if pd.isna(description):
        return False  # Handle missing values safely
    desc_lower = description.lower()
    if any(exclude in desc_lower for exclude in exclude_keywords):
        return False  # Exclude these items from being considered as liquids
    return any(keyword in desc_lower for keyword in liquid_keywords)

# Apply the filtering function to determine rows to remove
filtered_df = df[~df.iloc[:, 91].apply(is_liquid)]  # Use column index 91 (0-based index for column 92)

# Save the filtered data to a new CSV file
filtered_df.to_csv('habit_no_liquids_1.csv', index=False)

print("Filtered data saved to 'habit_no_liquids_1.csv'.")
