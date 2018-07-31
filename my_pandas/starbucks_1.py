import pandas as pd
import numpy as np
file_path = "./starbucks_store_worldwide.csv"
df = pd.read_csv(file_path)
print(df.head(1))
"""
       Brand  Store Number     Store Name Ownership Type     Street Address  \
0  Starbucks  47370-257954  Meritxell, 96       Licensed  Av. Meritxell, 96   

               City State/Province Country Postcode Phone Number  \
0  Andorra la Vella              7      AD    AD500    376818720   

                  Timezone  Longitude  Latitude  
0  GMT+1:00 Europe/Andorra       1.53     42.51  
"""
print("*"*20)
print(df.info())
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 25600 entries, 0 to 25599
Data columns (total 13 columns):
Brand             25600 non-null object
Store Number      25600 non-null object
Store Name        25600 non-null object
Ownership Type    25600 non-null object
Street Address    25598 non-null object
City              25585 non-null object
State/Province    25600 non-null object
Country           25600 non-null object
Postcode          24078 non-null object
Phone Number      18739 non-null object
Timezone          25600 non-null object
Longitude         25599 non-null float64
Latitude          25599 non-null float64
dtypes: float64(2), object(11)
memory usage: 2.5+ MB
None
"""
# grouped = df.groupby(by="Country")
# print(grouped)
# DataFrameGroupBy这个对象
# 可以遍历
# for i, j in grouped:
#     print(i)
#     print("-"*100)
#     print(j, type(j))
#     print("*"*100)
# df[df["Country"]="US"]
# 调用聚合方法
# country_count = grouped["Brand"].count()
# print(country_count["US"])
# print(country_count["CN"])

# 统计中国每个省店铺的数量
# print("*"*100)
# china_data = df[df["Country"] == "CN"]
# grouped = china_data.groupby(by="State/Province").count()["Brand"]
# print(grouped)
"""
State/Province
11    236
12     58
13     24
14      8
15      8
21     57
22     13
23     16
31    551
32    354
33    315
34     26
35     75
36     13
37     75
41     21
42     76
43     35
44    333
45     21
46     16
50     41
51    104
52      9
53     24
61     42
62      3
63      3
64      2
91    162
92     13
Name: Brand, dtype: int64
"""
# 数据按照多个条件进行分组,返回series
# grouped = df["Brand"].groupby(by=[df["Country"], df["State/Province"]]).count()
# print(grouped)
"""
Country  State/Province
AD       7                    1
AE       AJ                   2
         AZ                  48
         DU                  82
         FU                   2
         RK                   3
         SH                   6
         UQ                   1
AR       B                   21
         C                   73
         M                    5
         S                    3
         X                    6
AT       3                    1
         5                    3
         9                   14
AU       NSW                  9
         QLD                  8
         VIC                  5
"""
# print(type(grouped))
"""
<class 'pandas.core.series.Series'>
"""
# 数据按照多个条件进行分组,返回DataFrame
grouped1 = df[["Brand"]].groupby(by=[df["Country"], df["State/Province"]]).count()
print(grouped1, type(grouped1))
"""
                        Brand
Country State/Province       
AD      7                   1
AE      AJ                  2
        AZ                 48
        DU                 82
        FU                  2
        RK                  3
        SH                  6
        UQ                  1
AR      B                  21

[545 rows x 1 columns] <class 'pandas.core.frame.DataFrame'>
"""
# 索引的方法和属性
print("*"*10)
print(grouped1.index)
