# Regex Example

import re
txt = "My Name is Kunjan Patel"

# Search Method
x = re.search("\s",txt)  # Search for first whitespace character in the string
print("The First Whitespace character in location is : ",x.start())

