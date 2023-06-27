# Create Dictionary Using Two List

l1 = ['a','b','c','d','e','f']
l2 = [1,2,3,4,5,6]

my_dict = {k:v for k,v in zip(l1,l2)} # Using Zip Function
print(my_dict)
