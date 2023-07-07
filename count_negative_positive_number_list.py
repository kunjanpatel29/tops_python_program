"""
Write a Python Program for Count Negative, Positive numbers in a list.
"""


my_list = [10,20,-9,84,-5,-35,25,45,-75,72]


positive_num, negative_num = 0,0

for i in my_list:
        if i >=0:
            positive_num += 1
        else:
            negative_num += 1

print("Total Positive Number is : ",positive_num)
print("Total Negative Number is : ",negative_num)
