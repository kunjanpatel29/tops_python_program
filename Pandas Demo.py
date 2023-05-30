import numpy as np
import pandas as pd

dict1={
    "name":['Kunjan','Sanjay','Palak','Meet'],
    "marks":[90,85,78,65],
    "city":['Ahmedabad','Chennai ','Kolkata','Delhi ']
    }

# Calling DataFrame constructor on Dictionary
df=pd.DataFrame(dict1)
print(df)

df.to_csv('data.csv')

df.to_csv('data_index_false.csv',index=False)

# Display First Two row
print("\n",df.head(2))

# Display Last Two row
print(df.tail(2))

print("\n",df.describe())

# Creating empty series
ser = pd.Series()
print(ser)
 
# simple array
data = np.array(['K', 'U', 'N', 'J', 'A','N'])
   
ser = pd.Series(data)
print(ser)
