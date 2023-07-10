# Ways to Convert two lists into a dictionary


# initializing lists
keys = ["abc", "pqr", "bcd"]
values = [1, 4, 5]

# Printing original keys-value lists
print("Original key list is : " + str(keys))
print("Original value list is : " + str(values))

# to convert lists to dictionary
result = {}
for key in keys:
	for value in values:
		result[key] = value
		values.remove(value)
		break

# Printing resultant dictionary
print("Resultant dictionary is : " + str(result))


#  Using dictionary comprehension
keys = ["abc", "pqr", "bcd"]
values = [1, 4, 5]

