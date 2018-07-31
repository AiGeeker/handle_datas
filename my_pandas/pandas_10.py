import pandas as pd
import numpy as np
df1 = pd.DataFrame(np.ones((2, 4)), index=["A", "B"], columns=list("abcd"))
print(df1)
"""
     a    b    c    d
A  1.0  1.0  1.0  1.0
B  1.0  1.0  1.0  1.0
"""
print("*"*20)
df2 = pd.DataFrame(np.zeros((3, 3)), index=["A", "B", "C"], columns=list("xyz"))
print(df2)
"""
     x    y    z
A  0.0  0.0  0.0
B  0.0  0.0  0.0
C  0.0  0.0  0.0
"""
print("*"*20)
# 按照行索引合并
print(df2.join(df1))
"""
     x    y    z    a    b    c    d
A  0.0  0.0  0.0  1.0  1.0  1.0  1.0
B  0.0  0.0  0.0  1.0  1.0  1.0  1.0
C  0.0  0.0  0.0  NaN  NaN  NaN  NaN
"""
print("*"*20)
df3 = pd.DataFrame(np.zeros((3,3)),columns=list("fax"))
"""
    f    a    x
0  0.0  0.0  0.0
1  0.0  0.0  0.0
2  0.0  0.0  0.0
"""
df3 = pd.DataFrame(np.arange(9).reshape((3, 3)), columns=list("fax"))
print(df3)
"""
********************
   f  a  x
0  0  1  2
1  3  4  5
2  6  7  8
"""
print("*"*20)
print(df1.merge(df3, on="a"))
# 按照行相同的合并，内链接
"""
   a    b    c    d  f  x
0  1  1.0  1.0  1.0  0  2
1  1  1.0  1.0  1.0  0  2
"""
print("*"*20)
print(df1.merge(df3, on="a", how="outer"))
"""
     a    b    c    d  f  x
0  1.0  1.0  1.0  1.0  0  2
1  1.0  1.0  1.0  1.0  0  2
2  4.0  NaN  NaN  NaN  3  5
3  7.0  NaN  NaN  NaN  6  8
"""
print("*"*20)
# 左
print(df1.merge(df3, on="a", how="left"))
"""
********************
   a    b    c    d  f  x
0  1  1.0  1.0  1.0  0  2
1  1  1.0  1.0  1.0  0  2
"""
print("*"*20)
# 右
print(df1.merge(df3, on="a", how="right"))
"""
  a    b    c    d  f  x
0  1.0  1.0  1.0  1.0  0  2
1  1.0  1.0  1.0  1.0  0  2
2  4.0  NaN  NaN  NaN  3  5
3  7.0  NaN  NaN  NaN  6  8
"""
