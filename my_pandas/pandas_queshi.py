import pandas as pd
import numpy as np
f = pd.DataFrame(np.arange(12).reshape(3, 4), index=list("abc"), columns=list("WXYZ"))
print(f)
"""
   W  X   Y   Z
a  0  1   2   3
b  4  5   6   7
c  8  9  10  11
"""
print("*"*20)
f.iloc[1:, :1] = np.nan
print("*"*20)
print(f)
"""
     W  X   Y   Z
a  0.0  1   2   3
b  NaN  5   6   7
c  NaN  9  10  11
"""
print("*"*20)
# 判断是否为nan
print(pd.isnull(f))
"""
       W      X      Y      Z
a  False  False  False  False
b   True  False  False  False
c   True  False  False  False
"""
print("*"*20)
# 判断是否不为nan
print(pd.notnull(f))
"""
       W     X     Y     Z
a   True  True  True  True
b  False  True  True  True
c  False  True  True  True
"""
print("*"*20)
print(f[pd.notnull(f["W"])])
"""
     W  X  Y  Z
a  0.0  1  2  3
"""
print("*"*20)
print(f.dropna(axis=0, how="all"))
"""
     W  X   Y   Z
a  0.0  1   2   3
b  NaN  5   6   7
c  NaN  9  10  11
要所有的行为nan才会删除掉, inplace=True为原地修改的意思
"""
print("*"*20)
f.dropna(axis=0, how="any", inplace=True)
print(f)
d2 = [{"name":"xiaohong", "age":32, "tel":10010}, {"name":"xiaohang", "tel":10000}, {"name":"xiaowang","age":22}]
t4 = pd.DataFrame(d2)
print(t4)
"""
   age      name      tel
0  32.0  xiaohong  10010.0
1   NaN  xiaohang  10000.0
2  22.0  xiaowang      NaN
"""
print("*"*20)
print(t4.fillna(0))
"""
    age      name      tel
0  32.0  xiaohong  10010.0
1   0.0  xiaohang  10000.0
2  22.0  xiaowang      0.0
"""
print("*"*20)
print(t4.fillna(t4.mean()))
"""
 age      name      tel
0  32.0  xiaohong  10010.0
1  27.0  xiaohang  10000.0
2  22.0  xiaowang  10005.0
"""
print("*"*20)
print(t4["age"].fillna(t4["age"].mean()))
"""
0    32.0
1    27.0
2    22.0
"""