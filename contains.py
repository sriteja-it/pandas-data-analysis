import pandas as pd
data=["sriteja","raju","vinod","ganesh","prem "]
s=pd.Series(data)
print("\n series\n",s)
print("\nthe element is in:\n\n ",s.str.contains("sriteja"))