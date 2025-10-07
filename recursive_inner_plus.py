"""
Write the a python program that, given an input list of any level of complexity/nestedness, 
will return the inner most list plus 1. This is to be done with recursion. 
Note: the input will contain only integers or lists. 
"""

# %%
#input any list here
input_list= [1,2,3,4,[5,6,7,[8,9]]]
print(input_list)

# %%
# creat a recursion function to find the inner list
def find_inner_rec(input_list):
    for x in input_list: 
        if isinstance(x,list): 
            return find_inner_rec(x)
#now add one to the inner list
    return [x+1 for x in input_list]

# %%
print(find_inner_rec(input_list))


