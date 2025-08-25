import numpy as np
import pandas as pd
data=[21,55,67,87,100,np.nan]
s=pd.Series(data,index=["NUM1","NUM2","NUM3","NUM4","NUM5","NUM6"],dtype="object")
print("\n Series:\n\n",s)
print("\nfirst 5 Rows of a Series:\n",s.head())
print("\nfirst 6 Rows of a Series:\n",s.head(6))
print("\nlast 5 Rows of a Series:\n",s.tail())
print("\nlast 6 Rows of a Series:\n",s.tail(6))