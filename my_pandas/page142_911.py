"""
现在我们有2015到2017年25万条911的紧急电话的数据，
1.请统计出出这些数据中不同类型的紧急情况的次数，
2.如果我们还想统计出不同月份不同类型紧急电话的次数的变化情况，
应该怎么做呢？
"""
import pandas as pd
from matplotlib import  pyplot as plt
import numpy as np
df = pd.read_csv("./911.csv")
print(df.head(5))
"""
        lat        lng                                               desc  \
0  40.297876 -75.581294  REINDEER CT & DEAD END;  NEW HANOVER; Station ...   
1  40.258061 -75.264680  BRIAR PATH & WHITEMARSH LN;  HATFIELD TOWNSHIP...   
2  40.121182 -75.351975  HAWS AVE; NORRISTOWN; 2015-12-10 @ 14:39:21-St...   
3  40.116153 -75.343513  AIRY ST & SWEDE ST;  NORRISTOWN; Station 308A;...   
4  40.251492 -75.603350  CHERRYWOOD CT & DEAD END;  LOWER POTTSGROVE; S...   

       zip                    title            timeStamp                twp  \
0  19525.0   EMS: BACK PAINS/INJURY  2015-12-10 17:10:52        NEW HANOVER   
1  19446.0  EMS: DIABETIC EMERGENCY  2015-12-10 17:29:21  HATFIELD TOWNSHIP   
2  19401.0      Fire: GAS-ODOR/LEAK  2015-12-10 14:39:21         NORRISTOWN   
3  19401.0   EMS: CARDIAC EMERGENCY  2015-12-10 16:47:36         NORRISTOWN   
4      NaN           EMS: DIZZINESS  2015-12-10 16:56:52   LOWER POTTSGROVE   

                         addr  e  
0      REINDEER CT & DEAD END  1  
1  BRIAR PATH & WHITEMARSH LN  1  
2                    HAWS AVE  1  
3          AIRY ST & SWEDE ST  1  
4    CHERRYWOOD CT & DEAD END  1  
"""
print("*"*20)
print(df.info())
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 249737 entries, 0 to 249736
Data columns (total 9 columns):
lat          249737 non-null float64
lng          249737 non-null float64
desc         249737 non-null object
zip          219391 non-null float64
title        249737 non-null object
timeStamp    249737 non-null object
twp          249644 non-null object
addr         249737 non-null object
e            249737 non-null int64
dtypes: float64(3), int64(1), object(5)
memory usage: 17.1+ MB
None
"""
print("*"*20)
# 获取分类
print(df["title"].str.split(":"))
"""
0                  [EMS,  BACK PAINS/INJURY]
1                 [EMS,  DIABETIC EMERGENCY]
2                     [Fire,  GAS-ODOR/LEAK]
3                  [EMS,  CARDIAC EMERGENCY]
4                          [EMS,  DIZZINESS]
5                        [EMS,  HEAD INJURY]
6                    [EMS,  NAUSEA/VOMITING]
7              [EMS,  RESPIRATORY EMERGENCY]
8                   [EMS,  SYNCOPAL EPISODE]
9             [Traffic,  VEHICLE ACCIDENT -]
10            [Traffic,  VEHICLE ACCIDENT -]
11            [Traffic,  VEHICLE ACCIDENT -]
12            [Traffic,  VEHICLE ACCIDENT -]
13            [Traffic,  VEHICLE ACCIDENT -]
14            [Traffic,  VEHICLE ACCIDENT -]
15            [Traffic,  VEHICLE ACCIDENT -]
16             [EMS,  RESPIRATORY EMERGENCY]
17                         [EMS,  DIZZINESS]
18                  [EMS,  VEHICLE ACCIDENT]
19            [Traffic,  DISABLED VEHICLE -]
20            [Traffic,  VEHICLE ACCIDENT -]
21            [Traffic,  DISABLED VEHICLE -]
"""
temp_list = df["title"].str.split(":").tolist()
print(temp_list)
"""
[[],[],[]]
"""
print("*"*20)
cate_list = list(set([i[0] for i in temp_list]))
print(cate_list)
"""
['Traffic', 'Fire', 'EMS']
"""
print("*"*20)
# 构造全为0的数组
zeros_df = pd.DataFrame(np.zeros((df.shape[0], len(cate_list))), columns=cate_list)
print(zeros_df)
"""
        Fire  Traffic  EMS
0        0.0      0.0  0.0
1        0.0      0.0  0.0
2        0.0      0.0  0.0
3        0.0      0.0  0.0
4        0.0      0.0  0.0
5        0.0      0.0  0.0
6        0.0      0.0  0.0
7        0.0      0.0  0.0
8        0.0      0.0  0.0
9        0.0      0.0  0.0
........
........
"""
# 赋值
print("*"*20)
print(df["title"])
"""
0                  EMS: BACK PAINS/INJURY
1                 EMS: DIABETIC EMERGENCY
2                     Fire: GAS-ODOR/LEAK
3                  EMS: CARDIAC EMERGENCY
4                          EMS: DIZZINESS
5                        EMS: HEAD INJURY
6                    EMS: NAUSEA/VOMITING
7              EMS: RESPIRATORY EMERGENCY
8                   EMS: SYNCOPAL EPISODE
9             Traffic: VEHICLE ACCIDENT -
10            Traffic: VEHICLE ACCIDENT -
11            Traffic: VEHICLE ACCIDENT -
12            Traffic: VEHICLE ACCIDENT -
13            Traffic: VEHICLE ACCIDENT -
"""
# print("*"*20)
# # 赋值
for cate in cate_list:
    zeros_df[cate][df["title"].str.contains(cate)] = 1
    # 判断df["title"]里面是否含有cate里面的值，如果有，就赋值为0
    # break
print(zeros_df)
"""
       Fire  EMS  Traffic
0        0.0  1.0      0.0
1        0.0  1.0      0.0
2        1.0  0.0      0.0
3        0.0  1.0      0.0
4        0.0  1.0      0.0
5        0.0  1.0      0.0
6        0.0  1.0      0.0
7        0.0  1.0      0.0
8        0.0  1.0      0.0
9        0.0  0.0      1.0
10       0.0  0.0      1.0
11       0.0  0.0      1.0
12       0.0  0.0      1.0
13       0.0  0.0      1.0
14       0.0  0.0      1.0
......
......
"""
# for i in range(df.shape[0]):
#     zeros_df.loc[i, temp_list[i][0]] = 1
# print(zeros_df)
print("*"*20)
"""
1.请统计出出这些数据中不同类型的紧急情况的次数
"""
sum_set = zeros_df.sum(axis=0)
print(sum_set)






























