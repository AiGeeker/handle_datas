import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
file_path = "./IMDB-Movie-Data.csv"
df = pd.read_csv(file_path)

print(df.head(1))
"""
   Rank                    Title                    Genre  \
0     1  Guardians of the Galaxy  Action,Adventure,Sci-Fi   

                                         Description    Director  \
0  A group of intergalactic criminals are forced ...  James Gunn   

                                              Actors  Year  Runtime (Minutes)  \
0  Chris Pratt, Vin Diesel, Bradley Cooper, Zoe S...  2014                121   

   Rating   Votes  Revenue (Millions)  Metascore  
0     8.1  757074              333.13       76.0  

"""
print("*"*20)
print(df["Genre"])
"""
0         Action,Adventure,Sci-Fi
1        Adventure,Mystery,Sci-Fi
2                 Horror,Thriller
3         Animation,Comedy,Family
4        Action,Adventure,Fantasy
5        Action,Adventure,Fantasy
6              Comedy,Drama,Music
7                          Comedy
8      Action,Adventure,Biography
9         Adventure,Drama,Romance
"""
print("*"*20)
# 统计分类的列表
tem_list = df["Genre"].str.split(",").tolist() # [[],[],[]]
genre_list = list(set(list([i for j in tem_list for i in j])))
"""
['Sci-Fi', 'Comedy', 'War', 'Thriller', 'Romance', 'Musical', 'Adventure', 'Fantasy', 'Western', 
"""
print(genre_list)
print("****")
# 构造全为0的数组
print(df.shape[0]) # 由多少的行
print("*")
zeros_df = pd.DataFrame(np.zeros((df.shape[0], len(genre_list))), columns = genre_list)
# print(zeros_df)
# 给每个电影出现的分类进行相应的赋值1
for i in range(df.shape[0]):
    # zeros_df.loc[0, ["sci-fi", "Musicial"]] = 1
    zeros_df.loc[i, tem_list[i]] = 1

print(zeros_df.head(3))
"""
  Western  Music  Drama  Mystery  Action  Romance  Sci-Fi  Crime  Comedy  \
0      0.0    0.0    0.0      0.0     1.0      0.0     1.0    0.0     0.0   
1      0.0    0.0    0.0      1.0     0.0      0.0     1.0    0.0     0.0   
2      0.0    0.0    0.0      0.0     0.0      0.0     0.0    0.0     0.0   

   Horror  Family  Fantasy  History  War  Sport  Biography  Musical  \
0     0.0     0.0      0.0      0.0  0.0    0.0        0.0      0.0   
1     0.0     0.0      0.0      0.0  0.0    0.0        0.0      0.0   
2     1.0     0.0      0.0      0.0  0.0    0.0        0.0      0.0   

"""
print("*"*20)
# 统计每个分类的电影的数量和
genre_count = zeros_df.sum(axis = 0)
print(genre_count)
"""
Animation     49.0
Adventure    259.0
Action       303.0
Thriller     195.0
War           13.0
Fantasy      101.0
Family        51.0
Crime        150.0
Mystery      106.0
Comedy       279.0
Music         16.0
Biography     81.0
Musical        5.0
History       29.0
Romance      141.0
Drama        513.0
Sci-Fi       120.0
Western        7.0
Horror       119.0
Sport         18.0
dtype: float64
"""
# 排序
print("*"*20)
genre_count = genre_count.sort_values()
print(genre_count)
"""
Musical        5.0
Western        7.0
War           13.0
Music         16.0
Sport         18.0
History       29.0
Animation     49.0
Family        51.0
Biography     81.0
Fantasy      101.0
Mystery      106.0
Horror       119.0
Sci-Fi       120.0
Romance      141.0
Crime        150.0
Thriller     195.0
Adventure    259.0
Comedy       279.0
Action       303.0
Drama        513.0
dtype: float64
"""
# 画图
_x = genre_count.index
_y = genre_count.values
plt.figure(figsize=(20,8), dpi=80)
plt.bar(range(len(_x)), _y, width=0.4, color="orange")
plt.xticks(range(len(_x)), _x)
plt.show()