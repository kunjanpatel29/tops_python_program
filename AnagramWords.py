# Python Program for find anagram words

# Using Sorted
str1 = input("Enter the First String  = ")
str2 = input("Enter the Second String = ")

if(sorted(str1) == sorted(str2)):
    print("Two Strings are Anagrams.")
else:
    print("Two Strings are not Anagrams.")

# Using Counter
from collections import Counter

str1 = input("Enter the First String  = ")
str2 = input("Enter the Second String = ")

if(Counter(str1) == Counter(str2)):
    print("Two Strings are Anagrams.")
else:
    print("Two Strings are not Anagrams.")

# Without inbuilt methods
s1 = input("Enter First String : ")
s2 = input("Enter Second String : ")
count = 0
for i in s1:
    for j in s2:
        if i == j:
            count = count + 1

if count == len(s1):
    print("String are anagram of each other.")
else:
    print("String are not anagram of each other.")
