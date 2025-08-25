import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data={"Temperature":[12,25,23,94,39,83,56,78,86,79,70,98,77,68,69,57]
      ,"Humidity":[8,66,89,54,65,6,66,60,96,36,21,45,45,67,22,30],
      "Wind":[34,44,55,45,32,14,65,58,76,98,76,32,87,65,43,36],
      "precepitation":[54,23,55,69,6,76,6,96,84,35,89,26,42,17,97,65]}
df=pd.DataFrame(data)
print(df)
df.plot.area()
plt.show()