import pandas as pd
data1={'students':["sriteja","vinod","ganesh",'mahesh0',"varun","max"],"roll.no":[1,2,3,4,5,6],"age":[12,24,56,23,35,45]}
data2={'students':['chintu',"rani","raju"],"roll.no":[7,8,9],"age":[12,24,56]}
dataframe1=pd.DataFrame(data1)
dataframe2=pd.DataFrame(data2)
df=pd.concat([dataframe1,dataframe2])
print(df)