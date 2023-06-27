# Using Dictionary Comprehension

d = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F'}
remove_keys = [0,3,5]

my_dict = {k:v for k,v in d.items() if k not in remove_keys}
print(my_dict)
