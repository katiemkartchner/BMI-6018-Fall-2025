# %%
"""In this assignment you will experiment on your own. Using a health dataset of your choice (check with us if you are not sure),
write code to demonstrate the following Pandas functions:

Melt
Pivot
Aggregation
Iteration
Groupby"""

# %%
import pandas as pd
#import data on arrthmias from link: https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008

df= pd.read_csv('/Users/a14806/Desktop/diabetic_data.csv')

#print to view
df



# %%
#import IDS file that came with data for reference to better understand variables
dIDS=pd.read_csv('/Users/a14806/Desktop/IDS_mapping.csv')
dIDS

# %%
#Demonstrate Melt in pandas 

# I'm going to convert from “wide” to “long” format for some variables (in this case I'll unpivot time_in_hospital and admission_type_id)
melt = df.melt(
    id_vars=['race', 'gender', 'age', 'readmitted'], 
    value_vars=['time_in_hospital', 'admission_type_id'],
    var_name='metric', 
    value_name='value'
)
#do .head to see just the first few rows to make sure it is right
print(melt.head())

# %%
#Demonstrate Pivot in pandas
#I'll turn the melted data back into a wide format such as one row per (race, gender, age, readmitted) and columns for each metric
import pandas as pd

# import data
df= pd.read_csv('/Users/a14806/Desktop/diabetic_data.csv')

# Choose a few useful columns for the example
df_smallpivot = df[['gender', 'age', 'readmitted', 'time_in_hospital']].copy()

# Create a pivot table to find the average time_in_hospital for each gender and age group separated by whether they were readmitted or not
pivot_df = pd.pivot_table(
    df_smallpivot,
    index=['gender', 'age'],        # rows
    columns='readmitted',           # columns
    values='time_in_hospital',      # cell values
    aggfunc='mean',                 # aggregate function
    fill_value=0                    # replace missing cells with 0
)

print(pivot_df.head())

# %%
#demonstrate Aggregation



# Select a few relevant columns
df_smallagg = df[['gender', 'age', 'time_in_hospital', 'num_lab_procedures', 'num_medications']].copy()

# Group by gender and age, then aggregate multiple stats like the mean,min,max,sum, etc. 
agg_df = df_smallagg.groupby(['gender', 'age']).agg(
    avg_stay=('time_in_hospital', 'mean'),
    max_stay=('time_in_hospital', 'max'),
    min_stay=('time_in_hospital', 'min'),
    avg_labs=('num_lab_procedures', 'mean'),
    total_meds=('num_medications', 'sum'),
    patient_count=('time_in_hospital', 'count')
).reset_index()

print(agg_df.head())

# %%
#demonstrate iteration (going through one at a time)
#again using .head to see just the first few data points to verify it worked
# Select a few columns
df_smalliter = df[['patient_nbr', 'age', 'gender', 'time_in_hospital']].head(5)  # limit for display

# Iterate rows
print("Iterating rows")
for index, row in df_smalliter.iterrows():
    print(f"Patient {row['patient_nbr']} ({row['gender']}, {row['age']}): stayed {row['time_in_hospital']} days")

# Iterate columns
print("Iterating columns")
for col in df_smalliter.columns:
    print(f"Column: {col}")
    print(df_smalliter[col].head().tolist())

# %%
#demonstrate groupby (like iterate but can do all at once instead of one at a time)


# Select relevant columns
df_smallgroup = df[['gender', 'age', 'readmitted', 'time_in_hospital']].copy()

# Group by gender and readmission status
grouped = df_smallgroup.groupby(['gender', 'readmitted'])

# Compute summary statistics for each group (here we are grouping and aggregating the data at the same time) to show that the groupby worked
statssummary = grouped['time_in_hospital'].agg(['count', 'mean', 'min', 'max']).reset_index()

print(statssummary.head())



