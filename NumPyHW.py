# %%
"""1. Import numpy as np and print the version number."""
import numpy as np
print("1: Version of Numpy number: ",np.__version__ )

# %%
"""2. Create a 1D array of numbers from 0 to 9. Desired output:
 array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])"""
numpy_array = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print("2:",numpy_array)

# %%
"""3. Import a dataset with numbers and texts keeping the text intact in python numpy. Use the iris dataset available from https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.dataLinks to an external site."""


# Load the dataset from the URL
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# Import the data (calling it iris), keeping text columns as strings (dtype='object')
iris = np.genfromtxt(url, delimiter=',', dtype='object')

 # Show first 3 rows to show that it is keeping the original text intact
print("3: Import dataset and show first three rows to show text intact",iris[:3])

# %%
"""4. Find the position of the first occurrence of a value greater than 1.0 in petalwidth 4th column of iris dataset. Use the iris dataset available from https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.dataLinks to an external site.. (20 Points)"""
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
#make the type a float and then only use columns with float values 
iris = np.genfromtxt(url, delimiter=',', dtype=float, usecols=(0,1,2,3))

# Find first occurence where petal width (4th column) > 1.0
petal = np.where(iris[:, 3] > 1.0)[0]

# Get the first occurrence
first_occur = petal[0]
print("4:Position of first value > 1.0 in petal width column=", first_occur)

# %%
"""5. From the array a, replace all values greater than 30 to 30 and less than 10 to 10."""

np.random.seed(100)
a = np.random.uniform(1,50, 20)
#print to see starting numbers
print("5: origional numbers in arrary",a[:10])

# Replace values greater than 30 with 30 and less than 10 with 10
a[a > 30] = 30
a[a < 10] = 10
# print again to test that boolean mask worked correctly
print ("5: new values in boolean mask arrary",a[:10])



