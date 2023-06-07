# Return an iterator from a tuple, and print each value:
mytuple = ("Kunjan","Vikas","Sanjay","Prashant")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#Strings are also iterable objects, containing a sequence of characters:
mystr = "Python"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#Looping Through an Iterator

# Iterate the values of a tuple:
mytuple = ("Kunjan","Vikas","Sanjay","Prashant")

for x in mytuple:
  print(x)
