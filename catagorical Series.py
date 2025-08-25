import pandas as pd
s=pd.Series(["p","q","r","s"],dtype="category")
print(s)
s=s.cat.add_categories("t")
print("\nUpdate aa Categorier\n",s)
s=s.cat.remove_categories("s")
print("\n Remove the ctaegory element:\n",s)

