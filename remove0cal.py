import pandas as pd

#  Load the CSV file
df = pd.read_csv('updated_groups_1.csv')

#  Filter out rows where the 'KCAL' column is 0
filtered_df = df[df['KCAL'] != 0]


filtered_df.to_csv('701ready.csv', index=False)

# REMOVE 0 CALORIE

 