# Write a Python code To reverse words in a given string

string = input("Enter a String : ")

# reversing words in a given string
s = string.split()[::-1]
l = []
for i in s:
	l.append(i)

print(" ".join(l))


"""
string = input("Enter a String : ")

# reversing words in a given string
words = string.split(' ')
reverse_string = ' '.join(reversed(words))
print(reverse_string)
"""
