"""
1.使用matplotlib呈现出店铺总数排名前10的国家
2.使用matplotlib呈现出每个中国每个城市的店铺数量
"""
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager
my_font = font_manager.FontProperties(fname="/usr/share/fonts/truetype/arphic/uming.ttc")
file_path = "./starbucks_store_worldwide.csv"
df = pd.read_csv(file_path)
df = df[df["Country"] == "CN"]
print(df.head(1))
"""
          Brand  Store Number Store Name Ownership Type  \
2091  Starbucks  22901-225145  北京西站第一咖啡店  Company Owned   

                 Street Address City State/Province Country Postcode  \
2091  丰台区, 北京西站通廊7-1号, 中关村南大街2号  北京市             11      CN   100073   

     Phone Number                Timezone  Longitude  Latitude  
2091          NaN  GMT+08:00 Asia/Beijing     116.32      39.9  

"""
# 准备数据
data1 = df.groupby(by="City").count()["Brand"].sort_values(ascending=False)[:25]
_x = data1.index
_y = data1.values
# 画图
plt.figure(figsize=(20, 12), dpi=80)

plt.barh(range(len(_x)), _y, height=0.3, color="orange")
plt.yticks(range(len(_x)), _x, fontproperties=my_font)
plt.show()