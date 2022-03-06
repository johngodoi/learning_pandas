# 2. How to create a series from a list, numpy array and dict?
# Create a pandas series from each of the items below: a list, numpy and a dictionary Input

import numpy as np
import pandas as pd

mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))

print(pd.Series(mylist))
print(pd.Series(myarr))
print(pd.Series(mydict))
