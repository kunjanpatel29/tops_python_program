# Taken Input from the user
num = int(input("Enter a Number : "))

lst=[0,1]

[lst.append(lst[-2] + lst[-1]) for i in range(0,num)]

print(lst[:num])



