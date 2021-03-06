# 3. How to convert the index of a series into a column of a dataframe?
# Difficulty Level: L1 Convert the series ser into a dataframe with its index as another column on the dataframe.

import pandas as pd
import numpy as np
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
ser = pd.Series(mydict)

df = ser.to_frame().reset_index()
print(df.head())
