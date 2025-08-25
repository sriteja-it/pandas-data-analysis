import pandas as pd
marks={"math":[55,45,54,35,53],"sci":[23,43,44,23,44],"SOCIAL":[31,42,43,44,43]}
df=pd.DataFrame(marks)
print("\n marks of the students:\n",df)
print("\n sumof the data frame :\n",df.sum())
