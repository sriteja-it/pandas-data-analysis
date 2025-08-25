import pandas as pd
data1=[21,55,67,87,100]
data2=[34,44,66,78,86]
s1=pd.Series(data1)
s2=pd.Series(data2)
print("\n Series:\n\n",s1)
print("\n Series:\n\n",s2)
def demo(x1,x2):
    if(x1>x2):
        return x1
    elif(x1<x2):
       return x2
res=s1.combine(s2,demo)
print("\n combine two series:\n\n",res)
