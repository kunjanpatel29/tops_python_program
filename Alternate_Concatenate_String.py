# Alternate Concatenate String

s1 = input("Enter a String1 : ")
s2 = input("Enter a String2: ")

length1 = len(s1)
length2 = len(s2)
s2 = s2[::-1]

result = ""

for i in range(length1):
    if i < length1:
        result += s1[i]

    if i < length2:
        result += s2[i]
        
print(result)
