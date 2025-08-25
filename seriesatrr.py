import numpy as np
import pandas as pd
data=[21,55,67,87,100,np.nan]
s=pd.Series(data,name="MY SERIES IS NUMBER")
print("\n Series:\n\n",s)
print("\n\nSeries:",s.dtypes)
print("\n\nNumber of Dimentions:",s.ndim)
print("Size of the Series:",s.size)
print("\nReturn the name of the serirs:",s.name)
print("\nReturn the null value(t/f):",s.hasnans)