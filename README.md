# python-learn
## 简介
- 创造者：Guido van Rossum
- 时间：1989年圣诞节
- 定位：优雅、明确、简单。“The lift is short,I use python.”
- 特点：作为高级编程语言，提供了大量的第三库，可以提高开发效率；当然python也是解释型语言，所以运行速度慢；源码不能加密，发布产品即是发布源码。
## python 解释器（开源）
- CPython(官方解释器)
- IPython：基于CPython的交互式解释器，所以在交互方面有所增强
- PyPy：采用JIT技术，对Python代码进行动态编译，目的是提高Python的执行速度
- JPython：运行在Java平台的解释器，可以直接把Python代码编译成Java字节码执行。
- IronPython：运行在微软.Net平台上的Python解释器，可以直接把Python代码编译成.Net的字节码。
## 数据类型
- 整数
- 浮点数 如1.23e9 表示1.23x10^9
- 字符串，使用' '或者" "表示<br>如果需要显示' '，用" "包含即可；<br> 如需要显示" "，则使用转义字符 \\ ;<br> 如果需要多个转义字符，则使用r' '。
- 布尔值（true,false）运算（and,or,not）
- 空值（None）
## 变量
- 变量名必须是大小写英文、数字和_的组合，且不能用数字开头。
- 由于Python是动态语言，所以可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量。
## 常量
使用大写字母代表常量
## 除法运算
除法运算符`/`，得到的是浮点数;运算符`//`，得到的是整除数；而运算符`%`，得到的是余数。
（PS：在java中，只有当除数或者被除数有一个为浮点数，运算符`/`才得到浮点数；运算符`%`同样是取余数）
## 字符编码
### ASCII编码
- 8个bit作为一个字节，即一个字节能表示的最大的整数就是`255`（二进制11111111=十进制255）
### GB2312编码
- 补充ASCII编码的中文编码，至少使用两个字节处理中文
- 几乎全世界每种语言都有其对应的语言编码
### Unicode
- 将所有语言统一到一套编码，一般一个字符用两个字节表示

如：字母`A`用ASCII编码是十进制的`65`，二进制的`01000001`

而`A`的Unicode编码是`00000000 01000001`，即在ASCII前面补0即可。

### UTF-8
- 解决Unicode编码在存储和传输 英文字符 上比ASCII编码多一倍存储空间的缺陷
- “可变长编码”的UTF-8编码
    - 常用英文字符：1个字节(也就可以说UTF-8兼容ASCII编码)
    - 一般汉字字符：3个字节
    - 生僻字符：4-6个字节

如用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件
![记事本编码](https://cdn.liaoxuefeng.com/cdn/files/attachments/001387245992536e2ba28125cf04f5c8985dbc94a02245e000/0)
浏览网页的时候，服务器会把动态生成的Unicode内容转换为UTF-8再传输到浏览器（代码声明使用UTF-8:`<meta charset="UTF-8" />``）：
![浏览器编码](https://cdn.liaoxuefeng.com/cdn/files/attachments/001387245979827634fd6204f9346a1ae6358d9ed051666000/0)
## 字符串
- python3 版本的字符串是以Unicode编码的
- 字符与整数（十进制编码）的相互转换
    - 获取整数（编码）表示  `ord()`
    - 获取字符表示  `chr()`
    ```python
    print('A字符的编码表示',ord('A'))
    print('中字符的编码表示',ord('中'))
    print('编码65的字符表示',chr(65))
    ```
    ```
    A字符的编码表示 65
    中字符的编码表示 20013
    编码65的字符表示 A
    ```
- 字节类型`bytes`用带b前缀的单引号或双引号表示，我们在对字符串进行存储或者传输时就是使用字节类型`bytes`
- 字符串与字节的相互转换
    - 将字符串转成字节`encode()`,接收转换编码类型的字符表示
    ```python
    print('ABC'.encode('ascii'))
    print('中文'.encode('utf-8'))
    print('中文'.encode('ascii'))
    ```
    ```
    b'ABC'
    b'\xe4\xb8\xad\xe6\x96\x87'
        print('中文'.encode('ascii'))
    UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
    ```
    含有中文|的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。
    - 将字节流转换成字符`decode()`,接收解码类型的字符表示，还可以传入errors='ignore'忽略错误的字节
    ```python
    print(b'ABC'.decode('ascii'))
    print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))    
    print(b'\xe4\xb8\xad\xff'.decode('utf-8',errors='ignore'))
    ```
    ```
    ABC
    中文
    中
    ```
    - `len()`计算字符个数或者字节个数
- python 源码文件使用以下代码表明编码类型
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
```
第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；

第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
- 使用占位符
    - %d	整数
    - %f	浮点数
    - %s	字符串
    - %x	十六进制整数
    - %% 表示%
```python
print('Hello, %s' % 'world')
print("my name is %s,I'm  %d. " % ('joson',24))
print('growth rate: %d %%' % 7)

```
```
Hello, world
my name is joson,I'm  24.
growth rate: 7 %
```
## list 和 tuple
### list
- list 是可变的有序集合,使用`[]`定义集合，`len()`方法获取长度，`[index]`正序获取元素，`[-index]`倒序获取元素
```python
classmates = ['jack','mike','joson']
print('集合classmates 是 %s ,其长度为 %d ,第一个是 %s' % (classmates,len(classmates),classmates[0]))
print('倒数第一是 %s，倒数第二是 %s' % (classmates[-1],classmates[-2]))
```
```
集合classmates 是 ['jack', 'mike', 'joson'] ,其长度为 3 ,第一个是 jack
倒数第一是 joson，倒数第二是 mike
```
- list 的方法
  - append('str')  追加元素到末尾
  - insert(index,'str') 指定位置插入元素  
  - pop(index) 删除指定位置元素，不指定的话删除末尾元素
  - count('str')  指定元素出现的次数
  - clear() 清空集合
  - copy() 返回一个集合副本

```python
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
```
```
['jack', 'mike', 'joson', 'hason']
['jerry', 'jack', 'mike', 'joson', 'hason']
['jerry', 'jack', 'mike', 'joson']
hason 出现次数： 1
复制的集合： ['jerry', 'jack', 'mike', 'joson']
[]
```
### tuple
- tuple 是从定义开始就不可变的元组
  - count() 元素出现的次数
  - index() 元素第一次出现的位置
- 在定义一个元素的tuple时，应该在元素再加上逗号，免得与`()`运算混淆了，即`tuple = (1,)`
```python
tuple = ('a','b','c','a')
print(tuple)
print('c 出现的次数：',tuple.count('c'))
print('c 第一次出现在：',tuple.index('c'))
t1 = (1,)
t2 = (1)
print('元组t1:',t1)
print('整数t2:',t2)
```
```
('a', 'b', 'c', 'a')
c 出现的次数： 1
c 第一次出现在： 2
元组t1: (1,)
整数t2: 1
```
