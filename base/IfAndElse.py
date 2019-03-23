#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/3/23 22:21
# @Author : Joson
# @File   : IfAndElse.py

age = input('请输入你的年龄：')
if age:
    if int(age) < 18:
        print('你好，青少年！')
    elif int(age) < 50:
        print('你好，少年！')
    else:
        print('你好，老年人！')
else:
    print('未输入年龄，程序退出！')