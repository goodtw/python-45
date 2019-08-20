# coding=utf-8
import numpy as np

print('ndarray 对象测试begin')

a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b[1, 1] = 10
print(a.shape)
print(b.shape)
print(a.dtype)
print(b)

print('ndarray 对象测试end\n\n')

print('结构数组测试begin')
persontype = np.dtype({
    'names': ['name', 'age', 'chinese', 'math', 'english'],
    'formats': ['S32', 'i', 'i', 'i', 'f']})
peoples = np.array([("ZhangFei", 32, 75, 100, 90), ("GuanYu", 24, 85, 96, 88.5),
                    ("ZhaoYun", 28, 85, 92, 96.5), ("HuangZhong", 29, 65, 85, 100)],
                   dtype=persontype)
# 获取所有的年龄
ages = peoples[:]['age']
chineses = peoples[:]['chinese']
maths = peoples[:]['math']
englishs = peoples[:]['english']
# mean用来计算平均值
print(np.mean(ages))
print(np.mean(chineses))
print(np.mean(maths))
print(np.mean(englishs))
print('结构数组测试end\n\n')

# todo: ufunc

# arange 与linspace 都是创建等差数组；
# 区别是 arange类似于内置函数arange ,通过指定初始值，终止值，步长 来创建等差数组，默认不包括终止值；
# linspace 是linear space的缩写，意为线性等分向量，通过指定初始值，终止值，元素个数来创建的以为数组，默认包括终止值
print('创建连续数组begin')
x1 = np.arange(1, 11, 2)
x2 = np.linspace(1, 9, 5)
print(x1)
print(x2)
print('创建连续数组end\n\n')

print('算数运算begin')
# 加、减、乘、除、求 n 次方和取余数
print(np.add(x1, x2))
print(np.subtract(x1, x2))
print(np.multiply(x1, x2))
print(np.divide(x1, x2))
print(np.power(x1, x2))
print(np.remainder(x1, x2))
print('算数运算end\n\n')

print('计数组 / 矩阵中的最大值函数 amax()，最小值函数 amin()begin')
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.amin(a))
print(np.amin(a, 0))
print(np.amin(a, 1))
print(np.amax(a))
print(np.amax(a, 0))
print(np.amax(a, 1))
print('计数组 / 矩阵中的最大值函数 amax()，最小值函数 amin()end\n\n')

# axis=0 纵向看 axis=1 横向看
print('统计最大值与最小值之差 ptp()begin')
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.ptp(a))
# （1,4,7）（2,5,8）(3,6,9) 7-1=6
print(np.ptp(a, 0))
# （1,2,3） 3-1=2
print(np.ptp(a, 1))
print('统计最大值与最小值之差 ptp()end\n\n')

print('统计数组的百分位数 percentile()begin')
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.percentile(a, 50))
print(np.percentile(a, 50, axis=0))
print(np.percentile(a, 50, axis=1))
print('统计数组的百分位数 percentile()end\n\n')

print('统计数组中的中位数 median()、平均数 mean()begin')
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# 求中位数
print(np.median(a))
print(np.median(a, axis=0))
print(np.median(a, axis=1))
# 求平均数
print(np.mean(a))
print(np.mean(a, axis=0))
print(np.mean(a, axis=1))
print('统计数组中的中位数 median()、平均数 mean()end\n\n')

print('统计加权平均值 begin\n\n')
a = np.array([1, 2, 3, 4])
wts = np.array([1, 2, 3, 4])
print(np.average(a))
# 加权平均(1*1+2*2+3*3+4*4)/(1+2+3+4)=3
print(np.average(a, weights=wts))
print('统计加权平均值 end\n\n')

print('统计数组中的标准差 std()、方差 var() begin')
a = np.array([1, 2, 3, 4])
# 方差 mean((x - x.mean())** 2)
print(np.std(a))
print(np.var(a))
print('统计数组中的标准差 std()、方差 var() end\n\n')


print('NumPy 排序 begin')
a = np.array([[4, 3, 2], [2, 4, 1]])
print(np.sort(a))
print('\n')
print(np.sort(a, axis=None))
print('\n')
print(np.sort(a, axis=0))
print('\n')
print(np.sort(a, axis=1))
print('NumPy 排序 end\n\n')
