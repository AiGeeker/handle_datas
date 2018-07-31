import numpy  as  np
import random
# 使用numpy生成数组，得到ndarray的类型
t1 = np.array([1, 2, 3])
print(t1)
print(type(t1))


t2 = np.array(range(10))
print(t2)
print(type(t2))
t3 = np.arange(4,10,2)
print(t3)
print(type(t3))
# 数据中的类型
print(t3.dtype)
# numpy中的数据类型
#t4 = np.array(range(1, 4), dtype=float)
t4 = np.array(range(1, 4), dtype="i1")
print(t4)
print(t4.dtype)

# numpy中的bool类型
t5 = np.array([1,1,1,0,0], dtype=bool)
print(t5)
print(t5.dtype)
# 调整数据类型
t6 = t5.astype("int8")
print(t6)
print(t6.dtype)

# numpy中的小数
t7 = np.array([random.random() for i in range(10)])
print(t7)
print(t7.dtype)
# 保留小数
t8 = np.round(t7, 2)
print(t8)

t9 = np.arange(12)
print(t9)
print(t9.shape)
# 二维数组
t10 = np.array([[1,2,3], [4,5,6]])
print(t10)
print(t10.shape)
# 三维数组
t11 = np.array([[[1,2,3], [4,5,6]], [[7,8,9],[10,11,12]]])
print(t11)
print(t11.shape)

t12 = np.arange(12)
print(t12)
print(t12.reshape((3,4)))
# 2表示的是块，3表示的是每块的3行，4表示的是每块的列数
t13 = np.arange(24)
print(t13)
print(t13.reshape((2,3,4)))

t14 = t13.reshape(4,6)
print(t14)
# reshape是不会对数据本身进行修改，有返回值的操作
t15 = t14.reshape(t14.shape[0]*t14.shape[1],)
print(t15)

t16 = t14.flatten()
print(t16)

t17 = t16.reshape((1,24))
print(t17)

t18 = t16.reshape((24,1))
print(t18)

# 常用的转置
t2 = np.arange(24).reshape((4, 6))
print(t2)
print(t2.transpose())
print("*"*12)
print(t2.T)
print("*"*12)
print(t2.swapaxes(1,0))