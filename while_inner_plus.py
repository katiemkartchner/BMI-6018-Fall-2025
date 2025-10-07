# %%
"""
Write a python program that, given an input list of any level of complexity/nestedness, will return the inner most list plus 1. 
This is to be done with a while loop. Note: the input will contain only integers or lists. 
As an example:

input_list = [1,2,3,4,[5,6,7,[8,9]]]

your_py_program.py input_list

will produce:

[9,10]

That is [8, 9] (the inner most list) plus 1 -> [9, 10]
""" 

# %%
#change value of list to any list
input_list = [1,2,3,4,[5,6,7,[8,9]]]
print(input_list)

# %%
#while loop function called find_inner will find the inner most list within the list
def find_inner(input_list): 
    current_list=input_list
    #here we need to identify the first nested list
    while any(isinstance(x, list) for x in current_list):
        for x in current_list:
            if isinstance(x, list):
                current_list= x
                #current_list is now the inner most list so we break
                break
        #need to add 1 to the inner most list
    return [x + 1 for x in current_list]

# %%
print(find_inner(input_list)) 





