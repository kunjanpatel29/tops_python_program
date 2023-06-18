""" Lists are used to store multiple different types items in a single variable.
List items are ordered, changeable, and allow duplicate values."""

l = [1,2,1.1,1.2,"tops",True,10,320,1,2,"Python",False]

print(l)
l.append(100)      # Add Value in the last 
print(l)

#l.clear()         # Clear the list
#print(l)

l1 = l.copy()      # Copy Whole list from l to l1 
print(l)
print(l1)

l1.append(200)     # only add in l1 list
print(l)
print(l1)

l2 = l             # Assign whole list from l to l2
print(l2)
l2.append(300)     # Add value in l and l2 both list
print(l)
print(l2)

print(l.count(1))  # Return 3 Because True will consider as 1

l3 = [11,22,33]
l.extend(l3)       # Add l3-list Elements to the end of l-list
print(l)

print(l.index(10)) # Return index of 10 in list

l.insert(5,105)    # Add value in particular index in list 
print(l)

print(l.pop())     # By Default, Delete last value from the list
print(l)

print(l.pop(10))   # Remove Particular index value from the list
print(l)

l.remove(10)       # Remove Value from the list
print(l)

l.reverse()        # Reverse the list 
print(l)

for i in l:
    print(i)
print(201 in l)

# minimum item in list
print("Minimun Item in list is : ",min([1,2,3,4,5]))
 
# minimum item in dict
print("Minimun Item in Dictionary is : ",min({'a': 1, 'b': 2, 'c': 3}))
 
# minimum item in tuple
print("Minimun Item in Tuple is : ",min((7, 9, 11)))


#Finding the maximum of 3 integer variables
num1 = 4
num2 = 8
num3 = 2
 
max_val = max(num1, num2, num3)
print("Max Value is : ",max_val)

# Finding the maximum of 3 string variables
var1 = "kunjan"
var2 = "for"
var3 = "kunj"

max_val = max(var1, var2, var3)
print(max_val)
