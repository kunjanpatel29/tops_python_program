# Sorted Dictionary by value

my_dict = {'kunjan': 10, 'ashish': 9,
		'isha': 15, 'hanee': 2, 'suraj': 32}

mykeys = list(my_dict.keys())
mykeys.sort()
sorted_dict = {i: my_dict[i] for i in mykeys}

print(sorted_dict)
