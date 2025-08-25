import pandas as pd
data=["! Sriteja","\nraju\n\n","!vinod! ","\nganesh\t","!prem  "]
s=pd.Series(data)
print(s)
print("\n Strip from the both sdes:\n",s.str.strip("!\n\t"))
print("\nStrip from th left side\n\n",s.str.lstrip("!\n\t"))
print("\nStrip from th right side\n\n",s.str.rstrip("!\n\t"))
