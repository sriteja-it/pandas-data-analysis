import pandas as pd
df=pd.DataFrame({"Cat1":list("pqrs"),"cat2":list("pqrs"),"cat3":list("pqrs")},dtype="category")
print("\ndata frame=\n",df)
print("\n\ndatatypes of df:\n",df.dtypes)