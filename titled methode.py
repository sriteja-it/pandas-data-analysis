import pandas as pd
import numpy as np
data=["sriteja","raju","vinod","ganesh","prem ",np.nan]
s=pd.Series(data)
#Convert the camel
print('\n camel:\n',s.str.title())
print("\nlength of the element;\n",s.str.len())
print('\nCounting the :\n',s.count())