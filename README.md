# Introduction
这是《流程的Python》的读书笔记

# 第1章 Python数据类型
## 如何使用特殊方法
* 什么是Python的特殊方法
两边都是双下划线的方法，是特殊方法。如：`def __len__(self)`, `def __getitem__(self, position)`等。特殊方法的存在是为了被Python解释器调用的，自己不需要调用。如：一般不写`obj.__len__()`，而写`len(obj)`。<br>
很多时候，特殊方法的调用是隐式的，如`for i in x:`，其背后其实调用的是`iter(x)`，即`x.__item__()`。
* Python的特殊方法可以做什么
通过实现自定义类的特殊方法，可以像对内置类一样，操作自定义类，参考[代码](./code/data-model/french_deck.py)。

# 数据结构

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


