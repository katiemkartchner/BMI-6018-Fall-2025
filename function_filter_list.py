# %%
"""
Write a python program that, given an input list, will filter the input above a user defined threshold. 
This is to be done with a standard function.
That is, given a list [1,2,3,4,5,6,7,8,9], and an argument (6), it should return [1,2,3,4,5,6]
"""

# %%
#insert a list and a threshold
input_list=[1,2,3,4,5,6,7,8,9]
threshold=6
print("list:",input_list)
print("threshold:",threshold)

# %%
#make a standard function will filter the input above a user defined threshold
def filter_function(input_list, threshold):
    filter_list=[]
    for x in input_list: 
        if x <= threshold:
            filter_list.append(x)
    return(filter_list)
    

# %%
print(filter_function(input_list,threshold))


