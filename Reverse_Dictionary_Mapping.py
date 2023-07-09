# Reverse Dictionary Mapping

my_dict = {'a':10,'b':20,'c':30,'d':40,'e':50}
print(my_dict)  # Print Dictionary

# Reverse Mapping
result_dict = {value: key for key,value in my_dict.items()}
print(result_dict)
