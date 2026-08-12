import pandas as pd
temperature={"day1":30,"day2":40,"day3":70}
mymvr=pd.Series(temperature,index=["day1","day2"])
print(mymvr)