#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/3/20 22:07
# @Author : Joson
# @File   : ListAndTuple.py
classmates = ['jack','mike','joson']
print('集合classmates 是 %s ,其长度为 %d ,第一个是 %s' % (classmates,len(classmates),classmates[0]))
print('倒数第一是 %s，倒数第二是 %s' % (classmates[-1],classmates[-2]))

classmates.append('hason')
print(classmates)
classmates.insert(0,'jerry')
print(classmates)
classmates.pop()
print(classmates)
print('hason 出现次数：',classmates.count('joson'))
list = classmates.copy()
print('复制的集合：',list)
classmates.clear()
print(classmates)

print("------------------tuple---------------------")
tuple = ('a','b','c','a')
print(tuple)
print('c 出现的次数：',tuple.count('c'))
print('c 第一次出现在：',tuple.index('c'))
t1 = (1,)
t2 = (1)
print('元组t1:',t1)
print('整数t2:',t2)

print("-----------------练习----------------------")
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])