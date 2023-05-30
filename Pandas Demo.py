import numpy as np
import pandas as pd

dict1={
    "name":['Kunjan','Sanjay','Palak','Meet'],
    "marks":[90,85,78,65]
    }

# Calling DataFrame constructor on Dictionary
df=pd.DataFrame(dict1)
print(df)
