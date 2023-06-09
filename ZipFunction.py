# Python zip() with lists
name = [ "Kunjan", "Sanjay", "Vikas", "Keval" ]
roll_no = [ 4, 1, 3, 2 ]
mapped = zip(name, roll_no)
print(set(mapped))

#Python zip() with enumerate
names = ['Kunjan', 'Rohit', 'Sagar']
ages = [23, 24, 27]

for i, (name,age) in enumerate(zip(names,ages)):
    print(i,name,age)

#Python zip() with Tuple
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
zipped = zip(tuple1, tuple2)
result = list(zipped)
print(result)

#Python zip() with Multiple Iterables
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = ['x', 'y', 'z']
zipped = zip(list1, list2, list3)
result = list(zipped)
print(result)

# Example of unzip the values using zip
names = ['Kunjan', 'Rohit', 'Sagar']
ages = [23, 24, 27]

result = zip(names,ages)
resultlist = list(result)
print(resultlist)

c, v =  zip(*resultlist)  
print('c =', c)  
print('v =', v)  
