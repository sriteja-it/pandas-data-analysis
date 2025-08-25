import pandas as pd
data={'Student':["amit","john","jacob","vinod","sharon","varun"],'rank':[1,2,3,4,5,6],'marks':[45,76,36,35,25,40]}
df=pd.DataFrame(data,index=["rowa","rowb","rowc","rowd","rowe","rowf"])
print(df)
#transposeof the dataframe
print("\ntranseposep;\n",df.T)
print("first 5 rows;\n",df.head())
print("first 2 rows;\n",df.head(2))
print("first 6 rows;\n",df.head(6))
print("Last 5 row:\n",df.tail())
print("last 2 rows;\n",df.tail(2))


