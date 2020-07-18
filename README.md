# Introduction
这是《流程的Python》的读书笔记

# 第1章 Python数据类型
## 如何使用特殊方法
* 什么是Python的特殊方法
两边都是双下划线的方法，是特殊方法。如：`def __len__(self)`, `def __getitem__(self, position)`等。特殊方法的存在是为了被Python解释器调用的，自己不需要调用。如：一般不写`obj.__len__()`，而写`len(obj)`。<br>
很多时候，特殊方法的调用是隐式的，如`for i in x:`，其背后其实调用的是`iter(x)`，即`x.__item__()`。
* Python的特殊方法可以做什么
通过实现自定义类的特殊方法，可以像对内置类一样，操作自定义类，参考[代码](./code/data-model/french_deck.py)。
