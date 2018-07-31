import pandas as pd
import numpy as np
df = pd.DataFrame(np.ones((2, 4)), index=list("ab"), columns=list("abcd"))
print(df)
"""
a    b    c    d
a  1.0  1.0  1.0  1.0
b  1.0  1.0  1.0  1.0
"""
print("*"*20)
print(df.reindex(["a", "f"]))
"""
     a    b    c    d
a  1.0  1.0  1.0  1.0
f  NaN  NaN  NaN  NaN
"""
print("*"*20)
print(df.set_index("a"))
"""
 b    c    d
a                 
1.0  1.0  1.0  1.0
1.0  1.0  1.0  1.0
"""
print("*"*20)
print(df.set_index("a").index)
"""
Float64Index([1.0, 1.0], dtype='float64', name='a')
"""
print("*"*20)
print(df.set_index("a", drop=False))
"""
  a    b    c    d
a                      
1.0  1.0  1.0  1.0  1.0
1.0  1.0  1.0  1.0  1.0
不会舍弃原来的那一列
"""
print("*"*20)
print(df["d"].unique())
print("*"*20)
df.loc["a", "b"] =  100
print(df)
"""
  a      b    c    d
a  1.0  100.0  1.0  1.0
b  1.0    1.0  1.0  1.0
"""
print("*"*20)
print(df["b"].unique())
"""
[100.   1.]
"""
print("*"*20)
print(df.set_index(["b", "a"]).index)
"""
  MultiIndex(levels=[[1.0, 100.0], [1.0]],
           labels=[[1, 0], [0, 0]],
           names=['b', 'a'])  
"""
print("*"*20)
print(df.set_index(["b", "a", "c"], drop=False))
"""
                a      b    c    d
b     a   c                        
100.0 1.0 1.0  1.0  100.0  1.0  1.0
1.0   1.0 1.0  1.0    1.0  1.0  1.0
"""