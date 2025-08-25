import pandas as pd
data={"Id":["S01","S02","S03","S04","S05"],"Student":["Amit","John","Rahul","vinod",'Ganesh'],'Ranks':[1,2,3,4,5],"Marks":[90,65,86,45,23],
      "Address":["south","east","West","north","northwest"]}
df=pd.DataFrame(data)
print("\nDataFrame:\n",df)
print("\n\nselecting the columns:\n",df[df.columns[0:5]])#n-1\5-1