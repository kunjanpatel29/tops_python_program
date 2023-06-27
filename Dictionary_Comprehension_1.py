# Create Dictionary Using Two List

l1 = ['a','b','c','d','e','f']
l2 = [1,2,3,4,5,6]

my_dict = {k:v for k,v in zip(l1,l2)} # Using Zip Function
print(my_dict)

# Without using zip
my_dict = {l1[i]:l2[i] for i in range(len(l1))} 
print(my_dict)

"""
my_dict = {}
for i in range(len(l1)):
    my_dict[l1[i]] = l2[i]
print(my_dict)
"""
