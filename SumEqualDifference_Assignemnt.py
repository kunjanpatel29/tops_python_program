# Taken Input from the user
n1 = int(input("Enter Value of n1: "))
n2 = int(input("Enter Value of n2: "))

# Using If-Else
# Checking for if two values are equal or sum is 5 or difference is 5 Then Return True.
if n1 == n2 or (n1+n2) == 5 or abs(n1-n2) == 5:
    print("It is True")
else:
    print("It is False")


""" # Using Function
def SumorDifference(a,b):
    if a == b or abs(a-b) == 5 or (a+b) == 5:
        return True
    else:
        return False

n1 = int(input("Enter Value of n1: "))
n2 = int(input("Enter Value of n2: "))

print("It is ",SumorDifference(n1,n2)) """
