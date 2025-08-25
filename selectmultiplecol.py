import pandas as pd
data={"Student":["Amit","John","Rahul","vinod",'Ganesh'],'Ranks':[1,2,3,4,5],"Marks":[90,65,86,45,23]}
df=pd.DataFrame(data)

print("\nDataFrame:\n",df)
print("select the two col:\n",df[["Student","Marks"]])
