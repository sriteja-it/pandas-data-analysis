import pandas as pd
data=["Sriteja","Raju","Vinod","Ganesh","Prem "]
s=pd.Series(data)
print(s)
print("\n lowercase:\n\n",s.str.lower())
#print("\n uppercase:\n\n",s.str.upper())