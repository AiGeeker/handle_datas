from pymongo import MongoClient
import pandas as pd
import numpy as np

# client = MongoClient()
# collection = client["douban"]["tv1"]
# data = list(collection.find())
# print(data)
t3 = pd.DataFrame(np.arange(12).reshape(3,4), index=list("abc"),columns=list("WXYZ"))
print(t3)
"""
   W  X   Y   Z
a  0  1   2   3
b  4  5   6   7
c  8  9  10  11
"""
print("*"*20)
print(t3.loc["a", "Z"])
"""
3
"""
print(type(t3.loc["a", "Z"]))
"""
<class 'numpy.int64'>
"""
print("*"*20)
print(t3.loc["a", :])
"""
W    0
X    1
Y    2
Z    3
Name: a, dtype: int64
"""
print("*"*20)
print(t3.loc[:, "Y"])
"""
a     2
b     6
c    10
Name: Y, dtype: int64
"""
print("*"*20)
print(t3.loc[["a", "c"], :])
"""
********************
   W  X   Y   Z
a  0  1   2   3
c  8  9  10  11
"""
print("*"*20)
print(t3.loc[["a", "b"], ["W", "Z"]])
"""
*******************
   W  Z
a  0  3
b  4  7

"""

# iloc通过位置获取数据
print("*"*20)
print(t3)
"""
********************
   W  X   Y   Z
a  0  1   2   3
b  4  5   6   7
c  8  9  10  11
"""
print("*"*20)
print(t3.iloc[1])
"""
W    4
X    5
Y    6
Z    7
"""
print("*"*20)
print(t3.iloc[:, 2])
"""
a     2
b     6
c    10
Name: Y, dtype: int64
"""