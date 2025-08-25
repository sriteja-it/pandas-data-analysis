import pandas as pd
df=pd.read_csv("C:\\RecordsNew.csv")
print("\nexcel data:\n",df)
res=df["Marks"]
print("\nmarks of the students:\n",res)