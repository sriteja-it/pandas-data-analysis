import pandas as pd
marks={"math":[55,45,54,35,None,None,53],"sci":[23,43,None,44,None,23,44],"SOCIAL":[31,None,42,45,43,44,43]}
df=pd.DataFrame(marks)
print("\n marks of the students:\n",df)
print("\n count non empty values:\n",df.count())
print("\n print the max of the values:\n",df.max())
print("\n print the min of the values:\n",df.min())
print("\n mean of the eachy col will be:\n\n",df.mean())
print("\n mediAN of the marks each col:\n\n",df.median())
print("\n std of the marks each col:\n\n",df.std())
print("\n variance of the marks each col:\n\n",df.var())
print("\n summarry  of the statitics is:\n\n",df.describe())