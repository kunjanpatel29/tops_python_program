# Merge two Python dictionaries into one

d1 = {'one': 1, 'Two': 2, 'Three': 3}
d2 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

d3 = {**d1,**d2}
print(d3)
