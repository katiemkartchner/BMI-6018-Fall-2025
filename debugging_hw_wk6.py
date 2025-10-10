# %%
"""
1.a
Using the print() function only, get the wrong_add_function to print out where
it is making a mistake, given the expected output for ex, "we are making an error 
in the loop", which you would put near the loop. 
Structure the print() statement to show what the expected output ought to be
via f-strings: ie "The correct answer is supposed to be: [...]".
"""

# %%
def wrong_add_function(arg1,arg2):

   arg1_index=0
   while arg1_index < len(arg1):
      arg_2_sum = 0
      #print(arg1_index,arg_2_sum...check variable here for errors
      for arg2_elements in arg2:
         arg_2_sum = sum([arg1[arg1_index]+i for i in arg2])
         print("1.a",arg1_index,arg_2_sum,"The error is occuring in the inner for loop")
         #print to check variables here...errors were found so noted in the print statement
      arg1[arg1_index]=arg_2_sum 
      arg1_index+=1
   print("1.a",f"the code is wrong here-the expected value should be [2,3,4]; actual output: {arg1}")
   #f-string to show expected value and what is current output for this function
   return arg1

arg1 = [1,2,3]
arg2 = [1,1,1]

wrong_add_function(arg1, arg2)

# %%
"""
1.b
Then, changing as little as possible, modify the function, using the same 
general structure to output the correct answer. Call this new function 
correct_add_function() 
"""

# %%
def correct_add_function(arg1,arg2): 
    arg1_index = 0
    answer = []
    while arg1_index < len(arg1):
        for arg2_element in arg2:
            answer.append(arg1[arg1_index] + arg2_element)
            arg1_index += 1
    return answer

arg1 = [1, 2, 3]
arg2 = [1, 1, 1]
print("1.b",correct_add_function(arg1, arg2))

# %%

'''
2.a
Update the numeric section of the function with your changes from 1 for both 
2.b and 2.c
'''
def wrong_add_function(arg1,arg2):
   arg1_index = 0
   answer = []
   #numeric section
   if sum([type(i)==int for i in arg1])==len(arg1) and \
      sum([type(i)==int for i in arg2])==len(arg2):
         while arg1_index < len(arg1):
            for arg2_element in arg2:
               answer.append(arg1[arg1_index] + arg2_element)
            arg1_index += 1
         return answer
   #string section
   elif sum([type(i)==str for i in arg1])==len(arg1) and \
      sum([type(i)==str for i in arg2])==len(arg2):
         arg1_index=0
         while arg1_index < len(arg1):
            arg_2_sum = ''
            for arg2_elements in arg2:
               arg_2_sum += arg2_elements
            arg1[arg1_index]=arg1[arg1_index]+str(arg_2_sum)
            arg1_index+=1
         return arg1

arg_str_1=['1','2','3']
arg_str_2=['1','1', 1]

wrong_add_function(arg_str_1,arg_str_2)
print ("2.a","See above for new code with 1.b incorporated")


# %%

'''
2.b
Without modifying the string section code itself or the input directly, 
write a try, except block that catches the issue with the input below and 
returns an error message to the user, in case users give invalid inputs,
(for example an input of ["5","2", 5])
: "Your input argument [1 or 2] at element [n]
is not of the expected type. Please change this and rerun. Name this function 
exception_add_function()
'''
def wrong_add_function(arg1,arg2):

   #numeric section
   if sum([type(i)==int for i in arg1])==len(arg1) and \
      sum([type(i)==int for i in arg2])==len(arg2):
         arg1_index=0
         while arg1_index < len(arg1):
            arg_2_sum = 0
            for arg2_elements in arg2:
               arg_2_sum = sum([arg1[arg1_index]+i for i in arg2])
            arg1[arg1_index]=arg_2_sum  
            arg1_index+=1
         return arg1
   #string section
   elif sum([type(i)==str for i in arg1])==len(arg1) and \
      sum([type(i)==str for i in arg2])==len(arg2):
         arg1_index=0
         while arg1_index < len(arg1):
            arg_2_sum = ''
            for arg2_elements in arg2:
               arg_2_sum += arg2_elements
            arg1[arg1_index]=arg1[arg1_index]+str(arg_2_sum)
            arg1_index+=1
         return arg1
   
arg_str_1=['1','2','3']
arg_str_2=['1','1', 1]

wrong_add_function(arg_str_1,arg_str_2)

#create a function that will tell me if one of the inputs was a string
def exception_add_function(arg1, arg2):
    def first_mismatch(lst):
        if not lst:
            return None  
        expected = type(lst[0])
        for idx, v in enumerate(lst):
            if type(v) is not expected:
                return idx  # first wrong index
        return None

    try:
        result = wrong_add_function(arg1, arg2)
        if result is not None:
            return result  
        i1 = first_mismatch(arg1)
        if i1 is not None:
            return f"Your input argument 1 at element {i1} is not of the expected type. Please change this and rerun."
        i2 = first_mismatch(arg2)
        if i2 is not None:
            return f"Your input argument 2 at element {i2} is not of the expected type. Please change this and rerun."
        return "Your input arguments contain mixed or invalid types. Please correct and rerun."
    except TypeError:
        i1 = first_mismatch(arg1)
        if i1 is not None:
            return f"Your input argument 1 at element {i1} is not of the expected type. Please change this and rerun."
        i2 = first_mismatch(arg2)
        if i2 is not None:
            return f"Your input argument 2 at element {i2} is not of the expected type. Please change this and rerun."
        return "Your input arguments contain mixed or invalid types. Please correct and rerun."
print(exception_add_function(arg_str_1, arg_str_2))

# %%
'''
2.c
Without modifying the string section code itself or the input directly, 
write a try, except block that catches the issue with the input below and 
gets it to process via the string section. IE, do not, outside the function,
change the values of arg_str_1 or arg_str_2. Name this function 
correction_add_function(), i.e you will not be updating the wrong_add_function,
you will simply handle the error of wrong inputs in a seperate function, you want
the wrong_add_function to output its current result you are only bolstering the 
function for edge cases .
'''

# %%
def wrong_add_function(arg1,arg2):

   #numeric section
   if sum([type(i)==int for i in arg1])==len(arg1) and \
      sum([type(i)==int for i in arg2])==len(arg2):
         arg1_index=0
         while arg1_index < len(arg1):
            arg_2_sum = 0
            for arg2_elements in arg2:
               arg_2_sum = sum([arg1[arg1_index]+i for i in arg2])
            arg1[arg1_index]=arg_2_sum  
            arg1_index+=1
         return arg1
   #string section
   elif sum([type(i)==str for i in arg1])==len(arg1) and \
      sum([type(i)==str for i in arg2])==len(arg2):
         arg1_index=0
         while arg1_index < len(arg1):
            arg_2_sum = ''
            for arg2_elements in arg2:
               arg_2_sum += arg2_elements
            arg1[arg1_index]=arg1[arg1_index]+str(arg_2_sum)
            arg1_index+=1
         return arg1
   
arg_str_1=['1','2','3']
arg_str_2=['1','1', 1]

wrong_add_function(arg_str_1,arg_str_2)

def correction_add_function(arg1, arg2):
    #Calls the wrong_add_function and if error occur it retries by converting integers to strings so the string section runs
   
    try:
        output = wrong_add_function(arg1, arg2)
        if output is not None:
            return output
        # Mixed variable types: switch to strings and redo
        print("2.c",wrong_add_function([str(x) for x in arg1], [str(x) for x in arg2]))
    except TypeError:
        # Mixed types cause operation error: switch to strings and retry
        print("2.c",wrong_add_function([str(x) for x in arg1], [str(x) for x in arg2]))

correction_add_function(arg_str_1,arg_str_2)


