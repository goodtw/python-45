# coding=utf-8

# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。
# 解决方法为只要在文件开头加入 # -*- coding: UTF-8 -*- 或者 #coding=utf-8 就行了

## python2.7时使用 raw_input ，高版本下使用 input
name = input("What's your name?")
sum = 100+100
print('hello,%s' %name)
print('sum = %d' %sum)

#测试if
def testif(score):
    if score>= 90:
           print('Excellent')
    else:
           if score < 60:
               print('Fail')
           else:
               print('Good Job')

testif(100)

#测试for循环
def testfor():
    sum = 0
    for number in range(1,11,2):
        sum = sum + number
    print(sum)

testfor()


#测试while循环

def testwhile():
    sum = 0
    number = 1
    while number < 11:
        sum = sum + number
        number = number + 1
    print(sum)

testwhile()

#列表的使用
lists = ['a','b','c']
lists.append('d')
print(lists)
print(len(lists))
lists.insert(0,'mm')
lists.pop()
print(lists)

#元组的使用
tuples = ('tupleA','tupleB')
print(tuples[0])


# 定义一个 dictionary
score = {'guanyu':95,'zhangfei':96}
# 添加一个元素
score['zhaoyun'] = 98
print (score)
# 删除一个元素
score.pop('zhangfei')
# 查看 key 是否存在
print ('guanyu' in score)
# 查看一个 key 对应的值
print (score.get('guanyu'))
print (score.get('yase',99))


s = set(['a', 'b', 'c'])
s.add('d')
s.remove('b')
print (s)
print ('c' in s)


'''
这是多行注释，用三个单引号
这是多行注释，用三个单引号 
这是多行注释，用三个单引号
'''

'''
# 导入一个模块
import model_name
# 导入多个模块
import module_name1,module_name2
# 导入包中指定模块 
from package_name import moudule_name
# 导入包中所有模块 
from package_name import *
'''

def addone(score):
   return score + 1
print (addone(99))

#import scikit-learn


def sumNum():
    sum=0
    for number in range(1,99,2):
        sum = sum + number
    print(sum)


sumNum()

