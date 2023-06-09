# Return an iterator from a tuple, and print each value
mytuple = ("Kunjan","Vikas","Sanjay","Prashant")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#Strings are also iterable objects, containing a sequence of characters
mystr = "Python"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#Looping Through an Iterator

# Iterate the values of a tuple
mytuple = ("Kunjan","Vikas","Sanjay","Prashant")

for x in mytuple:
  print(x)

#Iterate the characters of a string
mystr = "Python"

for x in mystr:
  print(x)

# Return an iterator from a list, and print each value
mylist = [10,20,"Kunjan",5.4,30,"Python"]
myit = iter(mylist)

print("\n")
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#Looping Through an Iterator
# Iterate the values of a List
mylist = [10,20,"Kunjan",5.4,30,"Python"]

for x in mylist:
  print(x)
