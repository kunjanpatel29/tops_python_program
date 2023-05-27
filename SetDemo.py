""" Sets are used to store multiple items in a single variable. A set is a collection
which is unordered, unchangeable*, and unindexed. """

s = {1,2,1.1,1.2,"tops",10,320,1,2,"Python",False}
print(s)

s.add(9)         # Add an Element to the set
print(s)

s1=s.copy()      # Copy Whole list from s to s1
print(s1)

s.pop()          # Remove a random item from the set
print(s)

s.remove(320)    # Remove a Specified item from the set
print(s)

#s.clear()        # Clear the set  
#print(s)
