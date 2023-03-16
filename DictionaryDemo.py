d = {111:"Kunjan",899:"Vikas",423:"Sanjay",256:"Bhavesh",389:"Umang"}

print(d) # Print Dictionary in Curly Braces
d1 = d.copy() # Copy d to d1
print(d1)
#d.clear() # Clear Dictionary
#print(d)
print(d.get(111)) # Return Value of Key 111
print(d[256]) # Return Value of key 256
print(d.items()) # Return Dictionary Key With Values
print(d.keys()) # Return Only Dictionary Keys
print(d.values()) # Return Only Dictionary Values
print(d.pop(423)) # It will remove key and its value from dictionary
print(d)
print(d.popitem())# It will remove last key and value from dictionary
d2 = {326:"Jaimin",549:"Abhay",786:"Yesha",222:"Trushti"}
d.update(d2) # It will add new dictionary d2 in d
print(d)
d[699] = "Yash" # It will add in last of dictionary
print(d)

for i in d:
    print(i," : ",d[i])

#for i in d:
#    print(i)


