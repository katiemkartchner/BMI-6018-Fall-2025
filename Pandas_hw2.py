# %%
"""Question 1 (15 Points)
Compute the euclidean distance between series (points) p and q, without using a packaged formula.
Input"""
import pandas as pd
import numpy as np
p = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
q = pd.Series([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

#The Euclidean distance between two series (or points) p and q in an n-dimensional space is calculated by 
# the square root of the sum of the squared differences of their corresponding coordinates  or  d(p, q) = sqrt((p_1 - q_1)^2 + (p_2 - q_2)^2 + ... + (p_n - q_n)^2)

#First take the difference
difference = p - q
#Now square each of the values
squared_diff = difference**2
#now take the sum of the differences and find the square root
sum_of_squares = squared_diff.sum()
eu_distance=np.sqrt(sum_of_squares)
print("Question 1:",eu_distance)


# %%
"""Question 2 (15 Points)
Change the order of columns of a dataframe. Interchange columns 'a' and 'c'.
Input"""
df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))
df

# %%
# Get the column names
columns = df.columns.tolist()

# Interchange 'a' and 'c' in the list
# Find the indices of 'a' and 'c'
idx_a = columns.index('a')
idx_c = columns.index('c')

# Switch the column index
columns[idx_a], columns[idx_c] = columns[idx_c], columns[idx_a]

# Reindex the df
new_df= df[columns]

print("Question 2:",new_df)

# %%
"""Question 3 (15 Points)
Change the order of columns of a dataframe. Create a generic function to interchange two columns, without
hardcoding column names.
Input"""
df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))
print("Question 3: origional df:",df)
def swap_columns(df, col1_name, col2_name):

    # Get the column names
    cols = list(df.columns)

    # Find the indices of the columns to be swapped
    idx1 = cols.index(col1_name)
    idx2 = cols.index(col2_name)

    # Swap the column names in the list
    cols[idx1], cols[idx2] = cols[idx2], cols[idx1]

    # Reindex the DataFrame with the new column order
    return df[cols]

#test it out here to see if function swap_columns works
# Swap columns b and a in the df
    
df_swapped_test = swap_columns(df, 'b', 'a')
print("Swap Function test result:",df_swapped_test)


# %%
"""Question 4 (15 Points)
Format or suppress scientific notations in a pandas dataframe. Suppress scientific notations like ‘e-03’ in df and
print upto 4 numbers after decimal.
Input"""
df = pd.DataFrame(np.random.random(4)**10, columns=['random'])
print("Question 4:Origional data frame generated: ",df)

#Make scientific notation go away and kep 4 places after decimal
pd.set_option('display.float_format', lambda x: '%.4f' % x)
print("4 decimal places only:",df)


# %%

"""Question 5 (15 Points)
Create a new column that contains the row number of nearest column by euclidean distance. Create a new column
such that, each row contains the row number of nearest row-record by euclidean distance.
Input"""
df = pd.DataFrame(np.random.randint(1,100, 40).reshape(10, -1),columns=list('pqrs'), index=list('abcdefghij'))
print("create random data frame:",df)


import scipy.spatial.distance 
from scipy.spatial.distance import cdist

# Create the sample dataframe
df = pd.DataFrame(np.random.randint(1, 100, 40).reshape(10, -1), 
                  columns=list('pqrs'), 
                  index=list('abcdefghij'))

# Calculate pairwise euclidean distances between all rows
distances = cdist(df.values, df.values, metric='euclidean')

# For each row, find the nearest row 
nearest_rows = []
nearest_dists = []

for i in range(len(df)):
    # Set distance to itself as infinity to exclude it
    distances[i, i] = np.inf
    
    # Find index of minimum distance
    nearest_idx = np.argmin(distances[i])
    nearest_rows.append(df.index[nearest_idx])
    nearest_dists.append(distances[i, nearest_idx])

# Add new columns to dataframe
df['nearest_row'] = nearest_rows
df['dist'] = nearest_dists

print("Question 5: add dist and nearest_row:",df)


# %%

"""
Question 6 (15 Points)
Correlation is a statistical technique that shows how two variables are related. Pandas dataframe.corr() method is
used for creating the correlation matrix. It is used to find the pairwise correlation of all columns in the dataframe.
Any na values are automatically excluded. For any non-numeric data type columns in the dataframe it is ignored.
Input"""
data = {'A': [45, 37, 0, 42, 50],
'B': [38, 31, 1, 26, 90],
'C': [10, 15, -10, 17, 100],
'D': [60, 99, 15, 23, 56],
'E': [76, 98, -0.03, 78, 90]
}
df=pd.DataFrame(data)
print("Question 6:Orgional dataframe:",df)

print("correlation matrix:",df.corr())


