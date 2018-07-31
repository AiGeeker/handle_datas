import pandas as pd
t2 = pd.Series([1, 23, 2, 2, 1], index=list("abcde"))
print(t2)
print("*"*100)
temp_dict = {"name":"xiaohong", "age":30, "tel":10086}
t3 = pd.Series(temp_dict)
print(t3)
print(t3.dtype)
t2 = t2.astype(float)
print(t2)