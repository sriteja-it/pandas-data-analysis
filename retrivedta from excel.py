import pandas as pd
df=pd.read_csv("C:\\RecordsNew.csv",index_col="Student ID")
print(df.head())
print("\nexcel data:\n",df)
print("\n  the data from excel file;\n",df.loc[101])