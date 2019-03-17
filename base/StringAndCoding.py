#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2019/3/17 13:21
# @Author : Joson
# @File   : StringAndCoding.py
print('A字符的编码表示', ord('A'))
print('中字符的编码表示', ord('中'))
print('编码65的字符表示', chr(65))
print('----------------------------------')
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
print('中文'.encode('ascii', errors='ignore'))
print('----------------------------------')
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))
print('----------------------------------')
print('Hello, %s' % 'world')
print("my name is %s,I'm %d. " % ('joson', 24))
print('growth rate: %d %%' % 7)
