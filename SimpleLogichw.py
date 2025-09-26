# %%
# Logical Processing Homework

# %%
influenza_genome= [19, 15, 7, 9, 12, 6, 17, 20, 29, 14, 22, 8, 15, 12, 21, 25, 11, 10, 30, 4, 6, 24, 18, 21, 28, 22, 13, 19, 4, 23, 16, 25, 13, 28, 16, 29, 4, 3, 25, 13, 10, 26, 26, 18, 25, 28, 24, 18, 3, 9, 11, 29, 30, 16, 24, 5, 5, 25, 14, 7, 1, 15, 6, 6, 19, 19, 15, 2, 14, 7, 21, 5, 26, 25, 18, 18, 9, 7, 27, 4, 1, 23, 30, 25, 24, 29, 11, 16, 20, 15, 2, 9, 8, 13, 1, 13, 5, 17, 29, 25, 16, 13, 3, 30, 10, 21, 9, 18, 20, 14, 20, 19, 6, 4, 20, 5, 14, 5, 12, 27, 18, 28, 13, 30, 6, 9, 12, 9, 29, 4, 14, 22, 7, 25, 11, 12, 5, 24, 6, 3, 8, 3, 20, 24, 8, 23, 22, 11, 22, 10, 13, 14, 2, 6, 22, 22, 7, 6, 18, 28, 25, 4, 6, 24, 10, 24, 15, 18, 12, 24, 10, 16, 24, 21, 19, 24, 8, 8, 8, 10, 8, 15, 26, 14, 21, 18, 6, 10, 23, 2, 20, 15, 1, 4, 20, 8, 6, 1, 4, 15, 21, 26, 25, 1, 24, 15, 27, 8, 23, 4, 30, 22, 1, 3, 7, 16, 18, 29, 11, 4, 1, 29, 30, 16, 30, 10, 2, 26, 26, 7, 10, 15, 6, 25, 4, 7, 12, 24, 5, 8, 23, 16, 8, 3, 16, 1, 9, 4, 27, 26, 9, 25, 7, 14, 27, 21, 27, 28, 2, 2, 27, 22, 3, 23, 14, 16, 30, 12, 14, 8, 10, 5, 16, 12, 24, 3, 28, 9, 21, 7, 25, 9, 5, 3, 27, 7, 29, 25, 13, 11, 25, 21, 2, 14, 8, 17, 18, 23, 22, 12, 7, 26, 11, 25, 1, 23, 9, 12, 2, 4, 17, 27, 9, 13, 19, 15, 10, 12, 21, 25, 5, 1, 16, 17, 28, 23, 18, 10, 15, 18, 1, 11, 14, 10, 18, 12, 1, 23, 23, 25, 13, 27, 27, 6, 9, 11, 23, 6, 23, 14, 9, 15, 11, 24, 11, 29, 18, 6, 19, 16, 14, 26, 2, 14, 15, 25, 6, 21, 23, 25, 27, 5, 1, 17, 4, 7, 18, 8, 9, 10, 5, 21, 29, 9, 6, 2, 22, 12, 1, 13, 19, 6, 17, 21, 22, 26, 21, 10, 29, 8, 13, 10, 29, 6, 29, 16, 30, 5, 25, 14, 15, 15, 9, 24, 13, 5, 28, 18, 11, 21, 15, 12, 5, 16, 5, 29, 29, 29, 3, 10, 24, 16, 16, 12, 14, 6, 22, 21, 10, 10, 2, 14, 9, 29, 29, 2, 26, 11, 6, 7, 28, 10, 3, 24, 30, 2, 23, 9, 29, 27, 19, 1, 15, 11, 5, 7, 9, 26, 28, 27, 10, 20, 23, 29, 10, 15, 30, 13, 2, 11, 5, 9, 2, 30, 27, 14, 11, 20, 19, 1, 12, 10, 8, 6, 16, 3, 25, 5, 10, 24]
# 1.1 add 1 to the value at the index 300.
for x in range(len(influenza_genome)):
    if x == 300:
        influenza_genome[x] = influenza_genome[x]+1
        print("1.1:", influenza_genome[x])
# Only print the section of the array that is modified after completing each operation. i.e only print index 300 of the array after 1.1 and only the first 30 elements after 1.2


# %%
# 1.2 for the first 30 elements, if the value of the element is divisable by 3, multiply the value by 3.
for x in range(30):
    if influenza_genome[x] % 3 == 0:
        influenza_genome[x] = influenza_genome[x] * 3
print("1.2:", influenza_genome[:30])

# %%
# 1.3 for the last 30 elements, if the index value at that point is divisable by 5, replace the value with "a".
for x in range(-30,0):
    if influenza_genome[x] % 5 == 0:
        influenza_genome[x]="a"
print("1.3:", influenza_genome[-30:])

# %%
# 1.4 for all elements between index 200 and 300, if the value of the element is divisable by BOTH 3 AND 5, replace the value with the 10.
for x in range(200,300):
    if influenza_genome[x] % 5 == 0 and influenza_genome[x] % 3 == 0:
         influenza_genome[x]=10
print("1.4:", influenza_genome[200:300])

# %%
# Problem 2 Loops within loops
# Given the array influenza_genome, write code using both for and while loops that:

# 2.1 Create a for loop that iterates over items index 234 through 237 and prints each value (ie there should be 4 items)
for x in range(234, 238):  
    print("2.1:",influenza_genome[x])

# %%

# 2.2 Create a while loop that iterates over items index 234 through 237 and prints each value (ie there should be 4 items)

x = 234
while x <= 237:
    print("2.2:",influenza_genome[x])
    x = x + 1

# %%
# 2.3 Create a for loop that iterates over items index 234 through 237 and if the index is 236 print the item 7 times.
for x in range(234,238):
    if x==236:
        #print item at index 236 7 times
        print("2.3",influenza_genome[x])
        print("2.3",influenza_genome[x])
        print("2.3",influenza_genome[x])
        print("2.3",influenza_genome[x])
        print("2.3",influenza_genome[x])
        print("2.3",influenza_genome[x])
        print("2.3",influenza_genome[x])

# %%
# Problem 3 Functions
# You are going to implement 3 funtions that will process the influenza_genome list in various ways.

# 3.1 write a function, that takes in the array as an argument, and outputs 10 values from the dataset, spaced out by indexes that are 25 apart (ie 0, 25, 50, etc)
def my_function(arr):
    new_list = []
    for x in range(0, 250, 25): 
        new_list.append(arr[x])
    return new_list
print("3.1:",my_function(influenza_genome))

# %%
# 3.2 write a function that takes in the dataset as an argument and outputs 20 values from the dataset, spaced out by indexes that are y apart (ie you can decide how far apart they should be iterated as long as they dont exceed the length of the dataset)
def spaced_by_y(arr, y):
    results = []
    count = 0
    i = 0
    while count < 20 and i < len(arr):
        results.append(arr[i])
        i = i + y
        count = count + 1
    return results
print("3.2:",spaced_by_y(influenza_genome,24))

# %%
# 3.3 write a function that takes the output from the function from 3.2 as an argument, then only prints out every other item (ie there should only be 10 outputs)
#list from answer 3.2
output_list=[19, 28, 3, 26, 5, 18, 8, 12, 1, 18, 23, 14, 13, 9, 1, 14, 6, 25, 16, 23]
def every_other(output_list):
    for x in range(0, 20, 2):
        answer=output_list[x]
        print("3.3",answer)

every_other(output_list)


# %%
# Problem 4 Putting it all together
# Write a function that implements the code from problem 1.4, then implements the code from problem 2.3.
# The function should create a modified version of the influenza_genome list as per 1.4, then print the section described in problem 2.3. 

#code from 1.4: 
# 1.4 for all elements between index 200 and 300, if the value of the element is divisable by BOTH 3 AND 5, replace the value with the 10.
"""
for x in range(200,300):
   if influenza_genome[x] % 5 == 0 and influenza_genome[x] % 3 == 0:
       influenza_genome[x]=10
print("1.4:", influenza_genome[200:300])
"""

#code from 2.3: 
"""
# 2.3 Create a for loop that iterates over items index 234 through 237 and if the index is 236 print the item 7 times.
for x in range(234,238):
    if x==236:
        #print item at index 236 7 times
        print("2.3",influenza_genome[x])
        print("2.3",influenza_genome[x])
        print("2.3",influenza_genome[x])
        print("2.3",influenza_genome[x])
        print("2.3",influenza_genome[x])
        print("2.3",influenza_genome[x])
        print("2.3",influenza_genome[x])
"""
def four_list(arr):
    for i in range(200, 301):
        if arr[i] % 3 == 0 and arr[i] % 5 == 0:
            arr[i] = 10
    output = []
    for i in range(234, 238):
        if i == 236:
            for j in range(7):
                output.append(arr[i])
        else:
            output.append(arr[i])

    return output
four_answerlist = four_list(influenza_genome)
print("4.1:",four_answerlist)


