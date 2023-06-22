"""
Dictionary Comprehension : we have two lists named keys and value and we are iterating
over them with the help of zip() function.
"""

#Example
keys = ['a','b','c','d','e']
values = [1,2,3,4,5]

my_dict = {k:v for (k,v) in zip(keys,values)}
print(my_dict)

#Using fromkeys() Method
d = dict.fromkeys(range(5),True)
print(d)

# Using dictionary comprehension make dictionary
dic = {x:x**2 for x in range(1,6)}
print(dic)

d = {x.upper(): x*3 for x in "python"}
print(d)

# Using conditional statements in dictionary comprehension
my_dict = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(my_dict)

# Square of a Number
square_dict = {num: num*num for num in range(1, 11)}
print(square_dict)

key = ['j', 'k', 'l', 'm', 'n', 'o']  
value = [34, 54, 13, 76, 98, 74]  
d = dict (zip (key, value))  
print ("dict is : ",d)   

# Program : if a value is divisible by 6 then return True
lst = [12,5,18,36,20,56]
result = [True if x % 6 == 0 else False for x in lst]
#print(any(result))
print(all(result))
