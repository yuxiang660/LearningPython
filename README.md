<!-- TOC -->

- [Introduction](#introduction)
- [Python数据模型](#python数据模型)
    - [如何使用特殊方法](#如何使用特殊方法)
- [序列类型](#序列类型)
    - [列表list](#列表list)
    - [元组tuple](#元组tuple)
    - [切片slice](#切片slice)
    - [其他序列操作](#其他序列操作)
- [字典和集合](#字典和集合)
    - [泛映射类型](#泛映射类型)
- [文本和字节序列](#文本和字节序列)
    - [字节概要](#字节概要)
- [脚本编程与系统管理](#脚本编程与系统管理)

<!-- /TOC -->

# Introduction
这是《流畅的Python》和《Python Cookbook》的读书笔记

---

<p align="center">《流畅的Python》</p>
---

# Python数据模型
## 如何使用特殊方法
* 什么是Python的特殊方法
两边都是双下划线的方法，是特殊方法。如：`def __len__(self)`, `def __getitem__(self, position)`等。特殊方法的存在是为了被Python解释器调用的，自己不需要调用。如：一般不写`obj.__len__()`，而写`len(obj)`。<br>
很多时候，特殊方法的调用是隐式的，如`for i in x:`，其背后其实调用的是`iter(x)`，即`x.__item__()`。
* Python的特殊方法可以做什么
通过实现自定义类的特殊方法，可以像对内置类一样，操作自定义类，参考[代码](./code/data-model/french_deck.py)。

# 序列类型
* 常见的对序列类型的操作
迭代、切片、排序、拼接
* 按照内存排布分类
    * 容器序列（不连续，存引用，对存储类型无要求）
        * list, tuple, collections.deque
    * 扁平序列（连续，存值，对存储类型有要求）
        * str, bytes, array.array
* 按照是否可修改分类
    * 不可修改
        * tuple, str
    * 可修改
        * list, array.array
## 列表list
* 列表推导
可增加代码可读性，如下：
```python
# 不采用列表推导
symbols = 'abc'
codes = []
for symbol in symbols:
    codes.append(symbol)

# 采用列表推导
symbols = 'abc'
codes = [symbol for symbol in symbols]
```
    * 列表推导可替代filter与map
```python
# 列表推导
symbols = 'abcaA'
code = [s for s in symbols if ord(s) == 97]

# filter/map
symbols = 'abcaA'
code = list(filter(lambda s: s == 97, map(ord, symbols)))
```
* 生成器表达式
列表推导只能推导列表，如果想生成其他类型的**序列**，可以用生成器表达式。
```python
# 生成器表达式，生成tuple
symbols = 'abc'
tuple(ord(symbol) for symbol in symbols)
```
不同于列表推导，生成器表达式是逐个产出元素的。每次for循环，产生一个组合。

## 元组tuple
对数据的记录，数据的数量和位置信息也是很重要的。
* 两种作用
    * 不可变的列表
    * 没有字段名的记录
* 元组拆包
拆包可应用到任何可迭代对象，被拆包的元素数量必须和接受的元素数量一致，除非用`*`忽略
```python
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
# (0, 1, [2, 3, 4])
a, b, *rest = range(5)
# (0, [1, 2], 3, 4)
a, *body, c, d = range(5)
```
* Python3不可以把元组作为函数形参

## 切片slice
* 为什么切片和区间会忽略最后一个元素
可以类比C++的begin和end
* python解释器是如何理解切片操作的
```python
s = 'bicycle'
# 'bye'
s[::3]
# 'elcycib'
s[::-1]
# 'eccb'
s[::-2]
```
* 给切片赋值
```python
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l = list(range(10))
# [0, 1, 20, 30, 5, 6, 7, 8, 9]
l[2:5] = [20, 30]
# [0, 1, 20, 30, 5, 8, 9]
del l[5:7]
# [0, 1, 20, 11, 5, 22, 9]
l[3::2] = [11, 22]
# error
l[2:5] = 100
# [0, 1, 100, 22, 9]，对切片赋值，必须是可迭代的
l[2:5] = [100]
```
## 其他序列操作
* list.sort和sorted的区别
    * list.sort就地排序，返回None
    * sorted返回一个新的list

# 字典和集合
## 泛映射类型
* 哪些类型是可散列类型
    * 原子不可变类型：str、bytes和数值类型
    * frozenset
    * 元组，要求元组内所有元素都是可散列类型
* 常见的字典定义
```python
# a == b == c == d == e
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
```
* 字典推导
```python
DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan'),
]
country_code = {country: code for code, country in DIAL_CODES}
```
* 如何处理找不到的键
参见[code](./code/dict/index.py)
    * d[k]<br>
    如果找不到，会抛异常
    * d.get(k, default)<br>
    如果找不到，会返回default值替代
    * d.setdefault(k, default).append(value)<br>
    如果找不到，设置成默认值default，然后对默认值进行操作。相当于：
    ```python
    if key not in my_dict:
        my_dict[key] = []
    my_dict[key].append(new_value)
    ```
* 集合类型
    * set<br>
    不可散列
    ```python
    # set 的两种构造方法
    s = {1,2,3}
    s = set([1,2,3])
    ```
    * frozenset
    可散列，冻结后的集合不能再添加或删除任何元素
* 集合的推导
集合的推导和字典的推导是一样的，都是用花括号`{}`
```python
#{'§', '=', '¢', '#', '¤', '<', '¥', 'μ', '×', '$', '¶', '£', '©', '°', '+', '÷', '±', '>', '¬', '®', '%'}
from unicodedata import name
{chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i),'')}
```
* dict和set的背后：散列表    
    * 为什么 dict 的键和 set 元素的顺序是跟据它们被添加的次序而定的，以及为什么在映射对象的生命周期中，这个顺序并不是一成不变的？<br>
    因为Python会为字典扩容，往字典里添加新键可能会改变已有键的顺序。
    * 为什么不应该在迭代循环 dict 或是 set 的同时往里添加元素？<br>
    因为Python会为字典扩容，如果你在迭代一个字典的所有键的过程中同时对字典进行修改，那么这个循环很有可能会跳过一些键——甚至是跳过那些字典中已经有的键。因此，对字典的迭代和修改，要分两步做。

# 文本和字节序列
* 什么是Unicode<br>
Unicode把字符的标识（码位）和字节表述进行了区分：
    * Unicode标准以4~6个十六进制数字表示，如：A的码位是U+0041，高音谱号的码位是U+1D11E
    * 字符的具体表述（字节序列）取决于所用的编码：
        * UTF8-8编码中，A(U+0041)编码成单字节\x41，欧元符号(U+20AC)编码成三字节\xe2\x82\xac
        * 在UTF-16LE编码中，A(U+0041)编码成双字节\x41\x00，欧元符号(U+20AC)编码成两字节\xac\x20
把码位转化成字节序列的过程是编码；把字节序列转换成码位的过程是解码。
* `str`类型和`bytes`类型的区别
```python
s = 'café'
# 4
len(s)
# <class 'str'>
type(s)
b = s.encode('utf8')
# 5
len(b)
# b'caf\xc3\xa9'
print(b)
# <class 'bytes'>
type(b)
s2 = b.decode('utf8')
# 'café'
print(s2)
```
## 字节概要
`bytes`或`bytearray`对象的各个元素是介于 0~255（含）之间的整数，是一个二进制序列。
```python
cafe = bytes('café', encoding='utf_8')
# cafe: b'caf\xc3\xa9'
# 99, cafe[0]返回一个整数，99是'c'的字节编码
cafe[0]
# b'c', cafe[:1]返回长度为1的bytes对象（切片返回相同类型的序列）
cafe[:1]
cafe_arr = bytearray(cafe)
# cafe_arr: bytearray(b'caf\xc3\xa9')
# bytearray(b'\xa9'), cafe_arr[-1:]返回bytearray对象
cafe_arr[-1:]
```
* 如何显示二进制序列
虽然二进制序列其实是整数序列，但是它们的字面量表示法表明其中有ASCII 文本。因此，各个字节的值可能会使用下列三种不同的方式显示：
    * 可打印的ASCII字节（从空格到~），使用ASCII字符文本
    * 制表符、换行符、回车符和\对应的字节，使用转义序列\t、\n、\r和`\\`
    * 其他字节值，使用十六进制转义序列(例如，\x00表示空字节)
* 编解码错误的原因
    * 编码错误UnicodeEncodeError<br>
    编码的目的是将Unicode文本转换成字节序列
        * `utf8`或`utf16`可以编码任何Unicode字符串
        * 当某种编码方式无法编码某字符时，可选择报错、忽略、或者替换此字符的操作
    * 解码错误UnicodeDecodeError<br>
    解码的目的是将字节序列转换成Unicode文本，并不是所有字节序列都是有效的`utf8`或`utf16`。
        * 对于`utf8`或`utf16`解码方式，如果遇到无效的字节序列，会抛出异常
        * 对于很多陈旧的8位解码方式，如`iso8859_1`，即使解码失败也不会抛出异常，而是出现乱码

---
<p align="center">《Python Cookbook》</p>
---

# 脚本编程与系统管理

