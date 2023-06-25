# List
l1 = [1,2,3,4,5]
l2 = l1            # l1 and l2 are same
print(id(l1))   # Check Address Using id function
print(id(l2))
l2.remove(4)
print(l1)
print(l2)
