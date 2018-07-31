"""
统计出911数据中不同月份不同类型的电话的次数的变化情况
"""
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
# 把时间字符串转换为时间类型设置为索引
df = pd.read_csv("./911.csv")
print(df.head(2))
"""
        lat        lng                                               desc  \
0  40.297876 -75.581294  REINDEER CT & DEAD END;  NEW HANOVER; Station ...   
1  40.258061 -75.264680  BRIAR PATH & WHITEMARSH LN;  HATFIELD TOWNSHIP...   

       zip                    title            timeStamp                twp  \
0  19525.0   EMS: BACK PAINS/INJURY  2015-12-10 17:10:52        NEW HANOVER   
1  19446.0  EMS: DIABETIC EMERGENCY  2015-12-10 17:29:21  HATFIELD TOWNSHIP   

                         addr  e  
0      REINDEER CT & DEAD END  1  
1  BRIAR PATH & WHITEMARSH LN  1  
"""
print("*"*20)
df["timeStamp"] = pd.to_datetime(df["timeStamp"])

# 添加列，表示分类
temp_list = df["title"].str.split(":").tolist()
print(temp_list)
"""
[['EMS', ' VEHICLE ACCIDENT'], ['Fire', ' FIRE ALARM'], 
['Traffic', ' VEHICLE ACCIDENT -']]
"""
print("*"*20)
cate_list = [i[0] for i in temp_list]
print(cate_list)
"""
['EMS', 'Traffic', 'EMS', 'EMS', 'EMS', 'Fire', 'Traffic']
"""
print("*"*20)
print(np.array(cate_list).reshape((df.shape[0], 1)))
"""
[['EMS']
 ['EMS']
 ['Fire']
 ...
 ['EMS']
 ['Fire']
 ['Traffic']]
"""
print("*"*20)
df["cate"] = pd.DataFrame(np.array(cate_list).reshape((df.shape[0], 1)))
"""
对应的索引是数字
"""
df.set_index("timeStamp", inplace=True)
print(df.head(2))
"""
   lat        lng  \
timeStamp                                   
2015-12-10 17:10:52  40.297876 -75.581294   
2015-12-10 17:29:21  40.258061 -75.264680   

                                                                  desc  \
timeStamp                                                                
2015-12-10 17:10:52  REINDEER CT & DEAD END;  NEW HANOVER; Station ...   
2015-12-10 17:29:21  BRIAR PATH & WHITEMARSH LN;  HATFIELD TOWNSHIP...   

                         zip                    title                twp  \
timeStamp                                                                  
2015-12-10 17:10:52  19525.0   EMS: BACK PAINS/INJURY        NEW HANOVER   
2015-12-10 17:29:21  19446.0  EMS: DIABETIC EMERGENCY  HATFIELD TOWNSHIP   

                                           addr  e cate  
timeStamp                                                
2015-12-10 17:10:52      REINDEER CT & DEAD END  1  EMS  
2015-12-10 17:29:21  BRIAR PATH & WHITEMARSH LN  1  EMS  
"""
print("*"*20)
print("*"*20)
plt.figure(figsize=(20, 8), dpi=80)

# 分组
for group_name,group_data in df.groupby(by="cate"):
    # 对不同的分类进行绘画
    count_by_month = group_data.resample("M").count()["title"]
    # 画图
    _x = count_by_month.index
    print(_x)
    print("*"*20)
    # print(group_name)
    """
    DatetimeIndex(['2015-12-31', '2016-01-31', '2016-02-29', '2016-03-31',
               '2016-04-30', '2016-05-31', '2016-06-30', '2016-07-31',
               '2016-08-31', '2016-09-30', '2016-10-31', '2016-11-30',
               '2016-12-31', '2017-01-31', '2017-02-28', '2017-03-31',
               '2017-04-30', '2017-05-31', '2017-06-30', '2017-07-31',
               '2017-08-31', '2017-09-30'],
              dtype='datetime64[ns]', name='timeStamp', freq='M')
DatetimeIndex(['2015-12-31', '2016-01-31', '2016-02-29', '2016-03-31',
               '2016-04-30', '2016-05-31', '2016-06-30', '2016-07-31',
               '2016-08-31', '2016-09-30', '2016-10-31', '2016-11-30',
               '2016-12-31', '2017-01-31', '2017-02-28', '2017-03-31',
               '2017-04-30', '2017-05-31', '2017-06-30', '2017-07-31',
               '2017-08-31', '2017-09-30'],
              dtype='datetime64[ns]', name='timeStamp', freq='M')
DatetimeIndex(['2015-12-31', '2016-01-31', '2016-02-29', '2016-03-31',
               '2016-04-30', '2016-05-31', '2016-06-30', '2016-07-31',
               '2016-08-31', '2016-09-30', '2016-10-31', '2016-11-30',
               '2016-12-31', '2017-01-31', '2017-02-28', '2017-03-31',
               '2017-04-30', '2017-05-31', '2017-06-30', '2017-07-31',
               '2017-08-31', '2017-09-30'],
              dtype='datetime64[ns]', name='timeStamp', freq='M')
    """
    _y = count_by_month.values
    _x = [i.strftime("%Y%m%d") for i in _x]
    # EMS', 'Fire', 'Traffic'
    if group_name == "EMS":
        plt.plot(range(len(_x)), _y, label=group_name, color="orange")
    elif group_name == "Fire":
        plt.plot(range(len(_x)), _y, label=group_name, color="red")
    else:
        plt.plot(range(len(_x)), _y, label=group_name, color="blue")
plt.xticks(range(len(_x)), _x, rotation=90)
plt.legend(loc="best")
plt.show()

