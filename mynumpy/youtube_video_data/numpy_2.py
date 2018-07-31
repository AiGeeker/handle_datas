import numpy as np

us_file_path = "US_video_data_numbers.csv"
uk_file_path = "GB_video_data_numbers.csv"

t1 = np.loadtxt(us_file_path, delimiter=",", dtype="int", unpack=True)
t2 = np.loadtxt(us_file_path, delimiter=",", dtype="int")
#print(t1)
#print("*"*100)
print(t2)
print("*"*20)
# 取行
#print(t2[2])
# 取多行
#print("*"*20)
#print(t2[2:])
# 取不连续的多行
#print(t2[[2,8,10]])
#print(t2[1,:])
#print(t2[2:,:])
#print(t2[[2, 10, 3],:])
# 取列
#print(t2[:,0])
# 取连续的多列
#print(t2[:, 2:])

# 取不连续的多列
#print(t2[:, [0,2]])
# 取多行多列，取第三行，第四列的值
# a = t2[2,3]
# print(a)
# print(type(a))
#取多行多列，取第三行到第五行，第二列到第四列的结果
# 取的是行和列交叉点的位置
#print(t2[2:5,1:4])
# 取多个不相邻的点
# 选出来的结果是(0,0) (2,1) (2,3)
#c = t2[[0,2,2], [0,1,3]]
# print(c)
# t3 = np.arange(24).reshape((4,6))
# t3[t3>20] = 20
# print(t3)
# print(np.where(t3<=3,100,300))