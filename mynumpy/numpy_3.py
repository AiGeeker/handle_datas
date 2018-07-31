import numpy as np

us_data = "./youtube_video_data/US_video_data_numbers.csv"
uk_data = "./youtube_video_data/GB_video_data_numbers.csv"
# 加载国家信息
us_data = np.loadtxt(us_data,delimiter=",", dtype=int)
uk_data = np.loadtxt(uk_data, delimiter=",", dtype=int)
# 添加国家信息
#  构造全为0的数据
zeros_data = np.zeros((us_data.shape[0],1)).astype(int)
ones_data = np.ones((uk_data.shape[0],1)).astype(int)
# 分别添加一列全为0,1的数组
us_data = np.hstack((us_data,zeros_data))
uk_data = np.hstack((uk_data, ones_data))

# 拼接两组数据
final_data = np.vstack((us_data, uk_data))
print(final_data)

# 获取最大值或者最小值的位置,寻找行最大
t2 = np.array([[1,25,3],[3,1,7],[8,4,3]])
print(t2)
print(np.argmax(t2, axis=1))

print(np.random.randint(10,20,(4,5)))