my_list = ["Hello","My","Name","Is","Kunjan","Patel"]
print(my_list)

print(" ".join(my_list)) # Convert list to string use join function takes only string element

for i in my_list:
    print(i)

lst = [1,2,3,4,5]

a = " ".join(str(i) for i in lst)
print(a)

# Traversal of list function
my_list = ["Hello","My","Name","Is","Kunjan","Patel"]

string = ' '

for x in my_list:
    string += ' '+x

print(string)

# Using map
my_list = ["Hello","My","Name","Is","Kunjan","Patel",7,8,9]

string = ' '.join(map(str,my_list))

print(string)
