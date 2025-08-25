import pandas as pd
data={'Student':["amit","john","jacob","vinod","sharon"],'rank':[1,2,3,4,5],'marks':[45,76,36,35,25]}
df=pd.DataFrame(data,index=["rowa","rowb","rowc","rowd","rowe"])
print("datatypes of dataframe:\n\n",df.dtypes)
print("\nNumber of Dimensions:\n",df.ndim)
print("\nSize of the dataframe:\n",df.size)
print("\nShape of the DataFrame:\n",df.shape)
print("\nindex of df:\n",df.index)