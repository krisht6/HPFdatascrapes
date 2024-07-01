import pandas as pd

# Load the data
df = pd.read_csv('habit_no_liquids_1.csv')

# Initialize group identifier
df['group_ID'] = 0
current_group = 1

# Loop to assign group IDs based on 'FoodNum' and 'FoodType'
for i in range(len(df)):
    if i > 0:
        if df.at[i, 'FoodType'] == 2:
            df.at[i, 'group_ID'] = df.at[i - 1, 'group_ID']
        elif df.at[i, 'FoodNum'] != df.at[i - 1, 'FoodNum']:
            current_group += 1
    df.at[i, 'group_ID'] = current_group

# Define aggregation methods, ensuring conversion to string within the lambda
aggregation_methods = {df.columns[91]: lambda x: ' '.join(x.astype(str))}

# Include specified columns to take the first entry of each group
specified_columns = ['UserName', 'RecallNo', 'IntakeDate', 'Occ_Time', 'Occ_Name', 'FoodCode']
for col in specified_columns:
    aggregation_methods[col] = 'first'

# Sum numeric values for columns from 25 to 91
for col in df.columns[25:91]:
    if col in df.columns and df[col].dtype in ['int64', 'float64']:
        aggregation_methods[col] = 'sum'

# Perform the aggregation based on 'group_ID'
grouped = df.groupby('group_ID').agg(aggregation_methods)

# Rename the concatenated column for clarity if needed
grouped.rename(columns={df.columns[91]: 'GroupName'}, inplace=True)

# Save the aggregated data to a CSV file
grouped.to_csv('updated_groups_1.csv', index=False)

print("Grouping complete and file saved to 'updated_groups_1.csv'.")