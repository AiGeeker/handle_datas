import pandas as pd
file_path = "./IMDB-Movie-Data.csv"
df = pd.read_csv(file_path)
print(df.info())
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1000 entries, 0 to 999
Data columns (total 12 columns):
Rank                  1000 non-null int64
Title                 1000 non-null object
Genre                 1000 non-null object
Description           1000 non-null object
Director              1000 non-null object
Actors                1000 non-null object
Year                  1000 non-null int64
Runtime (Minutes)     1000 non-null int64
Rating                1000 non-null float64
Votes                 1000 non-null int64
Revenue (Millions)    872 non-null float64
Metascore             936 non-null float64
dtypes: float64(3), int64(4), object(5)
memory usage: 93.8+ KB
None
"""
print(df.head(1))
print("*"*20)
# 获取平均评分
print(df["Rating"].mean())
print("*"*20)
# 获取平均评分
print(df["Director"].tolist())
# 获取导演的人数
print("*"*20)
# print(len(set(df["Director"].tolist())))
"""
644
"""
print(len(df["Director"].unique()))
# 获取演员的人数
print("*"*20)
tem_actors_list = df["Actors"].str.split(",").tolist()
print(tem_actors_list)
"""
[['Chris Pratt', ' Vin Diesel', ' Bradley Cooper', ' Zoe Saldana'],
"""
print("*"*20)
actors_list = [i for j in tem_actors_list for i in j]
actors_num = len(set(actors_list))
print(actors_num)
"""
2394
"""
