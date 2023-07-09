# Display All Duplicate Items from a List

my_list = [10,20,30,20,40,10,60,70,80,30]
exist = {}
duplicates = []

for x in my_list:
    if x not in exist:
        exist[x] = 1
    else:
        duplicates.append(x)

print(duplicates)

