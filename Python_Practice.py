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

