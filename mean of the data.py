import pandas as pd
import numpy as np
data = {
    "Player": ["Sachin Tendulkar", "Virat Kohli", "Ricky Ponting", "Kane Williamson", "Joe Root"],
    "Years": [24, 16, 17, 14, 13],
    "Rank": [1, 2, 3, 4, 5],
    "Centuries": [100, 80, 71, 45, 45]}
df=pd.DataFrame(data)
print(df)
resdf=df.groupby("Years")
print("\n mean of the data:\n",resdf["Centuries"].agg(np.mean))