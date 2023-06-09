# Merge two Python dictionaries into one

# Using ** 
d1 = {'one': 1, 'Two': 2, 'Three': 3}
d2 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

d3 = {**d1,**d2}
print(d3)

# Using Copy and Update Method
d1 = {'one': 1, 'Two': 2, 'Three': 3}
d2 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

d3 = d1.copy()
d3.update(d2)
print(d3)
