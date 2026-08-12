import pandas as pd
z=[4,5,7,8]
data=pd.Series(z)
print(data)

x=(6,7,8,9)
collection=pd.Series(x)
print(collection)


y={"a":2,"b":5,"c":8}
values=pd.Series(y)
print(values)