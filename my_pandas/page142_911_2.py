"""
2.如果我们还想统计出不同月份不同类型紧急电话的次数的变化情况
"""
import pandas as pd
import numpy as np
file_path = "./911.csv"
df = pd.read_csv(file_path)
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
temp_list = df["title"].str.split(":").tolist()
print(temp_list)
"""
[['EMS', ' FALL VICTIM'], ['EMS', ' VEHICLE ACCIDENT'], ['Fire', ' FIRE ALARM'], ['Traffic', ' VEHICLE ACCIDENT -']]
"""
cate_list = [i[0] for i in temp_list]
print(cate_list)
"""
['Traffic', 'EMS', 'EMS', 'EMS', 'Traffic', 'Traffic', 'Traffic', 'Fire', 'EMS', 'Traffic', 
'Traffic', 'EMS', 'Fire', 'Fire', 'Traffic', 'EMS', 'EMS', 'Fire', 'EMS', 'EMS', 'EMS', 'Traffic', 'EMS', 'EMS', 
'EMS', 'Fire', 'Fire', 'Traffic', 'EMS', 'EMS', 'Traffic', 'EMS', 'EMS', 'EMS', 'Fire', 'Traffic',......]
"""
print("*"*20)
df["cate"] = pd.DataFrame(np.array(cate_list).reshape((df.shape[0], 1)))
print(df["cate"])
"""
0             EMS
1             EMS
2            Fire
3             EMS
4             EMS
5             EMS
6             EMS
7             EMS
8             EMS
9         Traffic
10        Traffic
11        Traffic
12        Traffic
13        Traffic
14        Traffic
15        Traffic
16            EMS
17            EMS
18            EMS
19        Traffic
20        Traffic
21        Traffic
22           Fire
23        Traffic
24        Traffic
25            EMS
26            EMS
27           Fire
28        Traffic
29        Traffic
"""
print("*"*20)
print(df.head(2))
"""
         lat        lng                                               desc  \
0  40.297876 -75.581294  REINDEER CT & DEAD END;  NEW HANOVER; Station ...   
1  40.258061 -75.264680  BRIAR PATH & WHITEMARSH LN;  HATFIELD TOWNSHIP...   

       zip                    title            timeStamp                twp  \
0  19525.0   EMS: BACK PAINS/INJURY  2015-12-10 17:10:52        NEW HANOVER   
1  19446.0  EMS: DIABETIC EMERGENCY  2015-12-10 17:29:21  HATFIELD TOWNSHIP   

                         addr  e cate  
0      REINDEER CT & DEAD END  1  EMS  
1  BRIAR PATH & WHITEMARSH LN  1  EMS  
"""
print("*"*20)
print(df.groupby(by="cate").count()["title"])
"""
cate
EMS        124840
Fire        37432
Traffic     87465
Name: title, dtype: int64
"""
