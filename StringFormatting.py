# Method 1: Formatting string using format() method

print('We all are {}.'.format('Friends'))
print('{1} {0}'.format('Programming','Python'))

print('a: {a},b: {b},c: {c}'.format(a=2,b='Python',c=9.2))
print('The valueof pi is: {0:1.5f}'.format(3.141592))
s1 = "My name is {fname}, I'm {age} Year's Old".format(fname = "Kunjan", age = 23)
print(s1)
txt2 = "My name is {0}, I'm {1}".format("Kunjan",23)
txt3 = "My name is {}, I'm {}".format("Kunjan",23)

# Method 2 : Formatting string using % operator

print("My name is %s Patel" %('Kunjan'))
x = 'looked'
print("Kunjan %s and %s around" %('walked',x))
print("I am %d Year's Old" %23)
print('Floating point numbers: %1.0f' %(13.144))

# Method 3: Formatted String using F-strings
name = 'Kunjan'
print(f"My name is {name}.")

num1 = 10
num2 = 9
print(f"Addition of num1 and num2 is {num1 + num2}")
print(f"Multiplication num1 and num2 is {num1 * num2}")

print(f"Square of Number is {(lambda x:x**2)(5)}")

