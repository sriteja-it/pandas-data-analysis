#joining two dataframes
import pandas as pd
data1={'students':["sriteja","vinod","ganesh",'mahesh0',"varun","max"],"roll.no":[1,2,3,4,5,6],"age":[12,24,56,23,35,45,]}
data2={"ranks":[5,6,4,7,2,8],"marks":[10,20,30,40,50,78]}
dataframe1=pd.DataFrame(data1)
dataframe2=pd.DataFrame(data2)
print(dataframe1)
print(dataframe2)
df=dataframe1.join(dataframe2)
print("joining the the two data Frames:\n",df)