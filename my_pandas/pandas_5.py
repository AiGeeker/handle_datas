import pandas as pd
df = pd.read_csv("./dogNames2.csv")
print(df)
print(df.head())
print("*"*100)
print(df.info())
print("*"*10)
# dataFrame中排序的方法,
df = df.sort_values(by="Count_AnimalName", ascending=False)
print(df.head(5))
"""
**********
      Row_Labels  Count_AnimalName
1156       BELLA              1195
9140         MAX              1153
2660     CHARLIE               856
3251        COCO               852
12368      ROCKY               823
"""
print("*"*109)
# pandas取行和列的注意点
# 方括号写数字，表示对行进行操作
# 写字符串，表示取列索引，对列进行操作
print(df[:20]) # 取前20个
"""
     Row_Labels  Count_AnimalName
1156       BELLA              1195
9140         MAX              1153
2660     CHARLIE               856
3251        COCO               852
12368      ROCKY               823
8417        LOLA               795
8552       LUCKY               723
8560        LUCY               710
2032       BUDDY               677
3641       DAISY               649
11703   PRINCESS               603
829       BAILEY               532
9766       MOLLY               519
14466      TEDDY               485
2913       CHLOE               465
14779       TOBY               446
8620        LUNA               432
6515        JACK               425
8788      MAGGIE               393
13762     SOPHIE               383
"""
print("*"*20)
print(df["Row_Labels"])
"""
1156              BELLA
9140                MAX
2660            CHARLIE
3251               COCO
12368             ROCKY
8417               LOLA
8552              LUCKY
"""
print("*"*30)
print(type(df["Row_Labels"]))
"""
<class 'pandas.core.series.Series'>
"""