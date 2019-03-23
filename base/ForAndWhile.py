#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/3/23 22:50
# @Author : Joson
# @File   : ForAndWhile.py
num = [0,1,2,3,4,5]
sum = 0
for n in num:
    sum = sum+n
print(num,'的和是：',sum)
print("----------------------------------------------")
num = range(101)
sum = 0
for n in num:
    sum = sum+n
print(num,'的和是：',sum)
print("----------------------------------------------")
sum = 0
num = 1
while num <= 99:
    sum = sum + num
    num = num + 2
print('99以内所有奇数的和：',sum)
print("----------------------------------------------")
n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print('END')
