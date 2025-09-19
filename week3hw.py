# Start your assignment here
print("Assignment 3")
print("Katie Kartchner")
print("Fall 2025")

#Problem 1: Lists, Sets and Coercion
# a. Create a list of integers no fewer than 10 items from 0 to 9
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("1.a:", lst)
# b. Add 3 to the 5th indexed element (index 5 → element = 5)
lst[4] += 3
print("1.b:", lst)
# c. Coerce all elements in the list to floats using list comprehension
lst_floats = [float(x) for x in lst]
print("1.c:", lst_floats)
# d. Coerce the list to a set
s = set(lst_floats)
print("1.d:", s)
# e. Using a method, append int 10 to the set
s.add(10)
print("1.e:", s)
# f. Using a method, pop an item from the set
popped_item = s.pop()
print("1.f: popped", popped_item, "→", s)
# g. Using a length counting function, count the number of items in the set
count_set = len(s)
print("1.g:", count_set)


# 2.a Combine the three sample dictionaries (given below) 
# into a nested dictionary (nested in programming means joined), named 
# two_a, ensure the key names are the same as the dictionary names.
    
two_patient_dictionary_kinoko = {
  "name" : "Kinoko",
  "year" : 2021
}
two_patient_dictionary_dango = {
  "name" : "Dango",
  "year" : 2019
}
two_patient_dictionary_mochi  = {
  "name" : "Mochi",
  "year" : 2020
}
two_a = {
    "kinoko": two_patient_dictionary_kinoko,
    "dango": two_patient_dictionary_dango,
    "mochi": two_patient_dictionary_mochi
}
print("2.a:", two_a)

# 2.b Using keys, retrieve the Dango's name from 2.a
print("2.b:", two_a["dango"]["name"])

# 2.c Using keys, update the value of Mochi's year to 2018. This should not be a variable
two_a["mochi"]["year"] = 2018
print("2.c:", two_a)

# 2.d Manually create a dictionary that has a single level and contains 
# each patient as the key and the year as the value. Set Mochi's year to 2019.'
two_d = {
    "Kinoko": 2021,
    "Dango": 2019,
    "Mochi": 2019
}
print("2.d:", two_d)

# 2.e Coerce the keys of 2.d into a list
two_e = list(two_d.keys())
print("2.e:", two_e)

# 2.f Coerce the values of 2.d into a list
two_f = list(two_d.values())
print("2.f:", two_f)

# 2.g Use the zip function to combine 2.e and 2.f into a dictionary again
two_g = dict(zip(two_e, two_f))
print("2.g:", two_g)


# Problem 3: Set combinations: Given the predefined sets below and using set methods

three_setA = {1, 2, 3, 4, 5}
three_setB = {2, 3, 4, 5, 6}
three_setC = {3, 5, 7, 9}
three_setD = {2, 4, 6, 8}
three_setE = {1, 2, 3, 4}

# 3.a Is set E a subset of set A
print("3.a:", three_setE.issubset(three_setA))

# 3.b Is set E a strict subset of set A
print("3.b:", three_setE < three_setA)

# 3.c Create a set that is the intersection of set A and set B
three_c = three_setA.intersection(three_setB)
print("3.c:", three_c)

# 3.d Create a set that is the union of sets C, D and E
three_d = three_setC.union(three_setD, three_setE)
print("3.d:", three_d)

# 3.e add 9 to the set
three_d.add(9)
print("3.e:", three_d)

# 3.f Using == compare this set to the list in one_a
print("3.f:", three_d == set(lst))

# 3.g Explain why they are not the same. What would you need to change if you wanted this to be True?
print("3.g:", """They are not the same because 'one_a' list contains numbers 0–9, but the union set contains only values from sets C, D, and E. Which is 1-9. 
      To make them equal, the sets would need to include all numbers 0–9.""")

# Problem 4: 
# 4.a Create a variable of type int with the value of 8
four_a = 8
print("4.a:",four_a)

# 4.b Create an empty list 
four_b = []
print("4b:",four_b)

# 4.c Using type(), add the type of 4.a to this list
four_b.append(type(four_a))
print("4.c:", four_b)

# 4.d Add 0.39 to 4.c
four_d = 0.39
four_b.append(four_d)
print("4.d",four_b)

# 4.e append the type of 0.39 to the list
four_b.append(type(four_d))
print("4.e:", four_b)

# 4.f exponentiate to the -10, ie: 4.d^-10,(hint: there might be an artihmetic operator to do so) 
# round it to no decimal places, and append to list.
four_f = round(four_d ** -10)
four_b.append(four_f)
print("4.f:", four_b)

# 4.g append the type to the list
four_b.append(type(four_f))
print("4.g:", four_b)

# Problem 5: More variable type changes. Continue from where you left off in Problem 4.

three_setA = {1, 2, 3, 4, 5}

# 5.a Manually create a dictionary where the values are items in the list from where 
# we left in  problem 4, and the keys should be their index in the list. Print the dictionary.
 
five_a = {
    "8": int,
    "0.39": float,
    "12284": int
}
print("5.a:",five_a)

# 5.b Add 300 and coerce it into a string
five_b = "300"
print("5.b",five_b)

# 5.c append the type to the list
four_b.append(type(five_b))
print("5.c:", four_b)

# 5.d slice the string up to the 2nd element
five_d = five_b[:2]
print ("5.d",five_d)

# 5.e append the type to the list
four_b.append(type(five_d))
print("5.e:", four_b)

# 5.f use list comprehension to convert this into a new list of integers
five_f = [int(x) for x in five_d]
print("5.f",five_f)

# 5.g append the type to the list
four_b.append(type(five_f))
print("5.g:", four_b)

# 5.h append the type of three_setA to the list
four_b.append(type(three_setA))
print("5.h:", four_b)


