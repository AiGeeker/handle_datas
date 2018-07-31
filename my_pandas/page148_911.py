import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
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
# 变成了pandas的时间类型了
df["timeStamp"] = pd.to_datetime(df["timeStamp"])
df.set_index("timeStamp", inplace=True)
print("*"*20)
print(df.head())
"""
                        lat        lng  \
timeStamp                                   
2015-12-10 17:10:52  40.297876 -75.581294   
2015-12-10 17:29:21  40.258061 -75.264680   
2015-12-10 14:39:21  40.121182 -75.351975   
2015-12-10 16:47:36  40.116153 -75.343513   
2015-12-10 16:56:52  40.251492 -75.603350   

"""
# 统计出911数据中不同月份电话次数
print("*"*20)
count_by_month = df.resample("M").count()["title"]
print(count_by_month)
"""timeStamp
2015-12-31     7916
2016-01-31    13096
2016-02-29    11396
2016-03-31    11059
2016-04-30    11287
2016-05-31    11374
2016-06-30    11732
2016-07-31    12088
2016-08-31    11904
2016-09-30    11669
2016-10-31    12502
2016-11-30    12091
2016-12-31    12162
2017-01-31    11605
2017-02-28    10267
2017-03-31    11684
2017-04-30    11056
2017-05-31    11719
2017-06-30    12333
2017-07-31    11768
2017-08-31    11753
2017-09-30     7276
"""
# 画图
_x = count_by_month.index
_y = count_by_month.values
# for i in _x:
#     print(dir(i))
#     break
"""
['__add__', '__class__', '__delattr__', '__dict__', '__dir__']查看所有的
datatime里面的方法
"""
_x = [i.strftime("%Y%m%d") for i in _x]
plt.figure(figsize=(20, 8), dpi=80)
plt.plot(range(len(_x)), _y)
plt.xticks(range(0,len(_x),20), list(_x)[::20], rotation=45)
plt.show()
