## 三个针对属性的方法 
说明：提供了三个方法的使用例，方便迅速了解。  
注意：下面关于方法的解释说明均来自于[官方文档](https://docs.python.org/zh-cn/3/library/functions.html?highlight=setattr#hasattr)，可点击自行查阅。
### 1.hasattr(object, name)
该实参是一个对象和一个字符串。如果字符串是对象的属性之一的名称，则返回 True，否则返回 False。（此功能是通过调用 getattr(object, name) 看是否有 AttributeError 异常来实现的。）
```python
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# file_name: use_hasattr.py
# author: ScCcWe
# time: 2019/12/30 9:20


class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


dog_bai = Animal("dog_bai", 12)
print(hasattr(dog_bai, 'name'))
print(hasattr(dog_bai, 'age'))
print(hasattr(dog_bai, 'jump'))
```
输出结果如下：
```bash
True
True
False
```
### 2.getattr(object, name[, default])
返回对象命名属性的值。name 必须是字符串。如果该字符串是对象的属性之一，则返回该属性的值。例如， getattr(x, 'foobar') 等同于 x.foobar。如果指定的属性不存在，且提供了 default 值，则返回它，否则触发 AttributeError。
```python
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# file_name: use_getattr.py
# author: ScCcWe
# time: 2019/12/30 9:35


class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


dog_bai = Animal("dog_bai", 12)
print(getattr(dog_bai, "name"))
print(getattr(dog_bai, 'age'))
print(getattr(dog_bai, 'width'))
```
输出结果如下：
```bash
dog_bai
12
Traceback (most recent call last):
  File "D:/hj/pycode/tools/md/1.py", line 17, in <module>
    print(getattr(dog_bai, 'width'))
AttributeError: 'Animal' object has no attribute 'width'
```
### 3.setattr(object, name, valule)
此函数与 getattr() 两相对应。 其参数为一个对象、一个字符串和一个任意值。 字符串指定一个现有属性或者新增属性。 函数会将值赋给该属性，只要对象允许这种操作。 例如，setattr(x, 'foobar', 123) 等价于 x.foobar = 123。
```python
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# file_name: use_setattr.py
# author: ScCcWe
# time: 2019/12/30 9:50


class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


dog_bai = Animal("dog_bai", 12)
print(getattr(dog_bai, "name"))
setattr(dog_bai, "name", "dog_black")
print(getattr(dog_bai, 'name'))

# 当属性不存在时，会自动创建
setattr(dog_bai, "height", 12)
print(getattr(dog_bai, "height"))
```
输出结果如下：
```bash
dog_bai
dog_black
12
```

## 通过分析colorama源码，体会三个方法的实际应用
### 安装colorama  
```commandline
pip install colorama
```
### 查看源码
说明：在pycharm中，将鼠标放在方法或者类上，使用`ctrl+鼠标左键`来查看方法源码  

新建一个py文件，输入下面的代码：
```python
# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: use_colorama.py
# author: ScCcWe
# time: 2020/5/29 21:49

from colorama import Back, init

init(autoreset=True)  # in windows
print(Back.BLACK + 'and with a green background')
```
我们查看一下Back的源码  
./ansi.py
```python
# Copyright Jonathan Hartley 2013. BSD 3-Clause license, see LICENSE file.
'''
This module generates ANSI character codes to printing colors to terminals.
See: http://en.wikipedia.org/wiki/ANSI_escape_code
'''

CSI = '\033['
OSC = '\033]'
BEL = '\007'


def code_to_chars(code):
    return CSI + str(code) + 'm'

def set_title(title):
    return OSC + '2;' + title + BEL

def clear_screen(mode=2):
    return CSI + str(mode) + 'J'

def clear_line(mode=2):
    return CSI + str(mode) + 'K'


class AnsiCodes(object):
    def __init__(self):
        # the subclasses declare class attributes which are numbers.
        # Upon instantiation we define instance attributes, which are the same
        # as the class attributes but wrapped with the ANSI escape sequence
        for name in dir(self):
            if not name.startswith('_'):
                value = getattr(self, name)
                setattr(self, name, code_to_chars(value))


class AnsiCursor(object):
    def UP(self, n=1):
        return CSI + str(n) + 'A'
    def DOWN(self, n=1):
        return CSI + str(n) + 'B'
    def FORWARD(self, n=1):
        return CSI + str(n) + 'C'
    def BACK(self, n=1):
        return CSI + str(n) + 'D'
    def POS(self, x=1, y=1):
        return CSI + str(y) + ';' + str(x) + 'H'


class AnsiFore(AnsiCodes):
    BLACK           = 30
    RED             = 31
    GREEN           = 32
    YELLOW          = 33
    BLUE            = 34
    MAGENTA         = 35
    CYAN            = 36
    WHITE           = 37
    RESET           = 39

    # These are fairly well supported, but not part of the standard.
    LIGHTBLACK_EX   = 90
    LIGHTRED_EX     = 91
    LIGHTGREEN_EX   = 92
    LIGHTYELLOW_EX  = 93
    LIGHTBLUE_EX    = 94
    LIGHTMAGENTA_EX = 95
    LIGHTCYAN_EX    = 96
    LIGHTWHITE_EX   = 97


class AnsiBack(AnsiCodes):
    BLACK           = 40
    RED             = 41
    GREEN           = 42
    YELLOW          = 43
    BLUE            = 44
    MAGENTA         = 45
    CYAN            = 46
    WHITE           = 47
    RESET           = 49

    # These are fairly well supported, but not part of the standard.
    LIGHTBLACK_EX   = 100
    LIGHTRED_EX     = 101
    LIGHTGREEN_EX   = 102
    LIGHTYELLOW_EX  = 103
    LIGHTBLUE_EX    = 104
    LIGHTMAGENTA_EX = 105
    LIGHTCYAN_EX    = 106
    LIGHTWHITE_EX   = 107


class AnsiStyle(AnsiCodes):
    BRIGHT    = 1
    DIM       = 2
    NORMAL    = 22
    RESET_ALL = 0

Fore   = AnsiFore()
Back   = AnsiBack()
Style  = AnsiStyle()
Cursor = AnsiCursor()
```
简单分析一下上述代码逻辑
- 我们调用的是一个对象实例Back（在源码结尾处Back = AnsiBack()）
- AnsiBack类继承于AnsiCodes类
- AnsiCodes类中调用setattr()给属性增加方法/值，给什么属性呢？给value属性，也就是BLACK，RED，GREEN等等的这些。所以在调用对象实例Back的属
性后，直接会触发code_to_chars()方法。

### 测试用例
源码的唯一难点就在于code_to_chars()这个方法，弄明白了这个方法，也就弄明白了源码的逻辑。  

下面我们编写一个测试用例来测试code_to_chars()方法：  
```python
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# file_name: test_use.py
# author: ScCcWe
# time: 2020/5/20 10:58


CSI = '\033['


def code_to_chars(code):
    print(CSI + str(code) + 'm')
    return CSI + str(code) + 'm'


code_to_chars(40)
```
![Image](https://github.com/ScCcWe/See_Then_Use/tree/master/img/测试用例结果.png)  

输出为一个背景颜色，说明上面的分析是对的。其实更加实际的情况是，你根据这个测试用例，去推测出源码的逻辑。而不是先推测逻辑，再去写测试用例。
这里为了分析的连贯性，我先写好了逻辑。  

### 总结
代码中使用getattr()和setattr()方法可以有效的减少代码的量，即便运行起来可能是一样的逻辑。
