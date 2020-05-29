# 断言assert
## 使用例
```python
# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: use_assert.py
# author: ScCcWe
# time: 2020/5/29 21:50

there_have_one_girl = '小花'
my_girl_friend = '小花'
# 期望相等
# 不符合期望，就会输出不相等
assert there_have_one_girl == my_girl_friend, '不相等'
```

## 使用场景
判断input的参数是否符合要求的类型：  
比如这里判断输入的`index`是否是`int`类型，如果不是会输出一个TypeError
```python
assert isinstance(index, int), 'TypeError'
```
注意！上述的代码作用等同于：
```python
if not isinstance(index, int):
    raise TypeError
```
