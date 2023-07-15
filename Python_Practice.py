# List
l1 = [1,2,3,4,5]
l2 = l1            # l1 and l2 are same
print(id(l1))   # Check Address Using id function
print(id(l2))
l2.remove(4)
print(l1)
print(l2)


# Ways to Remove Last Element From List
l = [10,20,5,15,30,40]
l.remove(40)  # Using remove Method
print(l)

#l.pop()     # Using pop Method
#print(l)

#del l[-1]   # Using del keyword
#print(l)

#a = l[:-1]  # Using Slicing
#print(a)

# Find Second Smallest Number in list
lst = [1,1,3,2]
l = list(set(lst))  #Use Set for remove duplicate value
print(l)   
print(l[1])  # Return Second Smallest Number

# Find Second Largest Number in list
lst = [1,1,3,2,5,9,8]
l = list(set(lst))
print(l)
print(l[-2])

#Lsit Slicing
lst = ['a', 'b', 'c', 'd']
print(lst[1:-1])
print(lst[-3:])
print(lst[:-3])

lst[0:2] =  'e'
print(lst)

# Dictionary
my_dict = {'a':1,'b':2,'c':3,'d':4}
print(my_dict)

print(my_dict.keys())
print(my_dict.values())

print(my_dict.items())
for i in my_dict.items():
    print(i)

print(my_dict['b'])  # Get Value for key

#print(my_dict['f'])  # If given key is not present then raise error
print(my_dict.get('f'))  # If given key is not preset then not raise error return None


d = 'a'+ '[a + b + c]'
print(d)

lst = [1,2,3,4]
lst1 = ['a','b','c']
result = lst+lst1
print(result)

print((2) ** 3)
#print((2,) ** 3)
print([] * 3)
#print({} * 3)
print(() * 3)

# Generate Error
#lst = ['x','y','z','w'] + "ab"
#print(lst)

# Not Generate Error
lst += "ab"
print(lst)

# String Example
mystr = "Hello How Are You"
print(mystr[6:9])
print(mystr.replace(" ",""))

# Print string each word first letter
words = mystr.split()
print(words)
for word in words:
    print(word[0],end="")
print()

# Number Pattern
num = int(input("Enter the Number of rows : "))
for i in range(1,num+1):
	for j in range(1,i+1):
		print(j,end="")
	print()
	
# Another Number Pattern	
num = int(input("Enter the Number of rows : "))
for i in range(num,0,-1):
	for j in range(1,i+1):
		print(j,end="")
	print()

# Pyramid Pattern(star)
nums = int(input("Enter the Number of rows : "))
for i in range(1,nums+1):
	for j in range(i):
		print("*",end="")
	print()

# Pyramid Another Pattern(star)
nums = int(input("Enter the Number of rows : "))
for i in range(nums,0,-1):
	for j in range(i):
		print("*",end="")
	print()



