import pandas as pd
data = {
    "Player": ["Sachin Tendulkar", "Virat Kohli", "Ricky Ponting", "Kane Williamson", "Joe Root"],
    "Years_of_Playing": [24, 16, 17, 14, 13],
    "Rank": [1, 2, 3, 4, 5],
    "Centuries": [100, 80, 71, 45, 45]}
df=pd.DataFrame(data)
print(df)
print(df.groupby('Player').groups)