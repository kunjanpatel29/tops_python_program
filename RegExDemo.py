# Regex Example

import re
txt = "My Name is Kunjan Patel"

# Search Method
x = re.search("\s",txt)  # Search for first whitespace character in the string
print("The First Whitespace character in location is : ",x.start())

x = re.search("pqr",txt) # Returns the none if no match
print(x)

  
# Split Method
b = re.split("\s",txt)
print(b)

b = re.split("\s",txt,1)  # Maxsplit parameter is last
print(b)
