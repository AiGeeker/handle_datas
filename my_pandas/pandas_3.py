import pandas as pd
import numpy as np
t1 = pd.DataFrame(np.arange(12).reshape((3,4)))
print(t1)
"""
   0  1   2   3
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
0  1   2   3代表列索引，0 1 2代表行索引
行索引，表明不同行，横向索引，叫index，0轴，axis=0
列索引，表名不同列，纵向索引，叫columns，1轴，axis=1
"""
t2 = pd.DataFrame(np.arange(12).reshape(3,4),index=list("abc"), columns=list("WXYZ"))
print(t2)

d1 = {"name":["xiaoming", "xiaohong"], "age":[20, 32], "tel":[10086, 10010]}
t3 = pd.DataFrame(d1)
print(t3)
"""
    age      name    tel
0   20  xiaoming  10086
1   32  xiaohong  10010
"""
d2 = [{"name":"xiaohong", "age":32, "tel":10010}, {"name":"xiaohang", "tel":10000}, {"name":"xiaowang","age":22}]
t4 = pd.DataFrame(d2)
print(t4)
"""
    age      name      tel
0  32.0  xiaohong  10010.0
1   NaN  xiaohang  10000.0
2  22.0  xiaowang      NaN
"""