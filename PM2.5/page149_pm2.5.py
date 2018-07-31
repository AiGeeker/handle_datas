"""
请绘制出5个城市的PM2.5随时间的变化情况

"""
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
file_path = "./BeijingPM20100101_20151231.csv"
df = pd.read_csv(file_path)
print(df.head(2))
"""
  No  year  month  day  hour  season  PM_Dongsi  PM_Dongsihuan  \
0   1  2010      1    1     0       4        NaN            NaN   
1   2  2010      1    1     1       4        NaN            NaN   
2   3  2010      1    1     2       4        NaN            NaN   
3   4  2010      1    1     3       4        NaN            NaN   
4   5  2010      1    1     4       4        NaN            NaN   

   PM_Nongzhanguan  PM_US Post  DEWP  HUMI    PRES  TEMP cbwd    Iws  \
0              NaN         NaN -21.0  43.0  1021.0 -11.0   NW   1.79   
1              NaN         NaN -21.0  47.0  1020.0 -12.0   NW   4.92   
2              NaN         NaN -21.0  43.0  1019.0 -11.0   NW   6.71   
3              NaN         NaN -21.0  55.0  1019.0 -14.0   NW   9.84   
4              NaN         NaN -20.0  51.0  1018.0 -12.0   NW  12.97   

   precipitation  Iprec  
0            0.0    0.0  
1            0.0    0.0  
2            0.0    0.0  
3            0.0    0.0  
4            0.0    0.0  
"""
print("*"*100)
print(df.info())
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 52584 entries, 0 to 52583
Data columns (total 18 columns):
No                 52584 non-null int64
year               52584 non-null int64
month              52584 non-null int64
day                52584 non-null int64
hour               52584 non-null int64
season             52584 non-null int64
PM_Dongsi          25052 non-null float64
PM_Dongsihuan      20508 non-null float64
PM_Nongzhanguan    24931 non-null float64
PM_US Post         50387 non-null float64
DEWP               52579 non-null float64
HUMI               52245 non-null float64
PRES               52245 non-null float64
TEMP               52579 non-null float64
cbwd               52579 non-null object
Iws                52579 non-null float64
precipitation      52100 non-null float64
Iprec              52100 non-null float64
dtypes: float64(11), int64(6), object(1)
"""
# 把分开的时间字符串通过periodIndex的方法转换为pandas的时间类型
period = pd.PeriodIndex(year=df["year"], month=df["month"], day=df["day"], hour=df["hour"], freq="H")
print(period)
"""
PeriodIndex(['2010-01-01 00:00', '2010-01-01 01:00', '2010-01-01 02:00',
             '2010-01-01 03:00', '2010-01-01 04:00', '2010-01-01 05:00',
             '2010-01-01 06:00', '2010-01-01 07:00', '2010-01-01 08:00',
             '2010-01-01 09:00',
             ...
             '2015-12-31 14:00', '2015-12-31 15:00', '2015-12-31 16:00',
             '2015-12-31 17:00', '2015-12-31 18:00', '2015-12-31 19:00',
             '2015-12-31 20:00', '2015-12-31 21:00', '2015-12-31 22:00',
             '2015-12-31 23:00'],
            dtype='period[H]', length=52584, freq='H')
"""
print(type(period))
print("*"*20)
"""
<class 'pandas.core.indexes.period.PeriodIndex'>
"""
df["datetime"] = period
print(df.head(5))
"""
PM_Nongzhanguan  PM_US Post  DEWP  HUMI    PRES  TEMP cbwd    Iws  \
0              NaN         NaN -21.0  43.0  1021.0 -11.0   NW   1.79   
1              NaN         NaN -21.0  47.0  1020.0 -12.0   NW   4.92   
2              NaN         NaN -21.0  43.0  1019.0 -11.0   NW   6.71   
3              NaN         NaN -21.0  55.0  1019.0 -14.0   NW   9.84   
4              NaN         NaN -20.0  51.0  1018.0 -12.0   NW  12.97   

   precipitation  Iprec         datetime  
0            0.0    0.0 2010-01-01 00:00  
1            0.0    0.0 2010-01-01 01:00  
2            0.0    0.0 2010-01-01 02:00  
3            0.0    0.0 2010-01-01 03:00  
4            0.0    0.0 2010-01-01 04:00  
"""
print("*"*20)
# 把datetime设置为索引
df.set_index("datetime", inplace=True)
# 进行降采样
df = df.resample("7D").mean()
print(df.shape)
print(df)
"""
              No    year  month   day  hour  season   PM_Dongsi  \
datetime                                                           
2010-01     372.5  2010.0    1.0  16.0  11.5     4.0         NaN   
2010-02    1080.5  2010.0    2.0  14.5  11.5     4.0         NaN   
2010-03    1788.5  2010.0    3.0  16.0  11.5     1.0         NaN   
2010-04    2520.5  2010.0    4.0  15.5  11.5     1.0         NaN   
2010-05    3252.5  2010.0    5.0  16.0  11.5     1.0         NaN   
2010-06    3984.5  2010.0    6.0  15.5  11.5     2.0         NaN   
2010-07    4716.5  2010.0    7.0  16.0  11.5     2.0         NaN   
2010-08    5460.5  2010.0    8.0  16.0  11.5     2.0         NaN   
2010-09    6192.5  2010.0    9.0  15.5  11.5     3.0         NaN   
2010-10    6924.5  2010.0   10.0  16.0  11.5     3.0         NaN   
2010-11    7656.5  2010.0   11.0  15.5  11.5     3.0         NaN   
2010-12    8388.5  2010.0   12.0  16.0  11.5     4.0         NaN   
2011-01    9132.5  2011.0    1.0  16.0  11.5     4.0         NaN  
"""
print("*"*20)
# 处理缺失数据，删除缺失数据
print(df["PM_US Post"])
"""
2010-01-01 00:00      NaN
2010-01-01 01:00      NaN
2010-01-01 02:00      NaN
2010-01-01 03:00      NaN
2010-01-01 04:00      NaN
2010-01-01 05:00      NaN
2010-01-01 06:00      NaN
2010-01-01 07:00      NaN
2010-01-01 08:00      NaN
2010-01-01 09:00      NaN
2010-01-01 10:00      NaN
2010-01-01 11:00      NaN
2010-01-01 12:00      NaN
2010-01-01 13:00      NaN
2010-01-01 14:00      NaN
2010-01-01 15:00      NaN
2010-01-01 16:00      NaN
2010-01-01 17:00      NaN
2010-01-01 18:00      NaN
2010-01-01 19:00      NaN
2010-01-01 20:00      NaN
2010-01-01 21:00      NaN
2010-01-01 22:00      NaN
2010-01-01 23:00    129.0
2010-01-02 00:00    148.0
2010-01-02 01:00    159.0
.....
.....
"""
data = df["PM_US Post"]
data_china = df["PM_Dongsihuan"]

# 绘图
_x = data.index
_x = [i.strftime("%Y%m%d") for i in _x]
_y = data.values

_x_china = data_china.index
_x_china = [i.strftime("%Y%m%d") for i in _x_china]
_y_china = data_china.values

plt.figure(figsize=(20, 8), dpi=80)
plt.plot(range(len(_x_china)), _y_china, label="CN_POST")
plt.plot(range(len(_x)), _y, label="US_POST")
plt.xticks(range(0, len(_x), 10), list(_x)[::10], rotation=45)
plt.legend(loc="best")
plt.show()
