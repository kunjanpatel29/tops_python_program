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
