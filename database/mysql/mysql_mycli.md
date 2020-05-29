## ascii
### 输出字符的ascii码
```python
print(ord('a'))
print(ord('A'))
```
输出结果为：97  
输出结果为：65

### ascii码对照
a-z: 97-122  
A-Z: 65-90  
空格：32  
空：0

### 输出字符串
```python
print(chr(65))
```
输出结果为: A

## file write
写入当前文件夹下的一个txt文件
````python
with open('./wrong.txt', 'a+', encoding='utf-8') as f:
    f.write(data + '\n')
````

## server in one line
启动一个server，用以分享当前路径下的文件
```python
python -m http.server 8888
```
访问方式：
```web
ip:8888
```

## define a func what_is_life()
./life.py
```python
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# file_name: life.py
# author: ScCcWe
# time: 2020/4/18 16:57


def what_is_life(want, time):
    for get in time:
        if get is want:
            return
        continue
```
./ScCcWe.py
```python
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# file_name: ScCcWe.py
# author: ScCcWe
# time: 2020/3/26 19:58


class ScCcWe:
    def __init__(self):
        self.start = 0
    
    @staticmethod
    def get_random_article(**kwargs):
        if kwargs['name'] == 'zhuangzi':
            with open('./quqie.txt', "r", encoding='utf-8') as f:
                data = f.readlines()
            print(data)
        elif kwargs['name'] == 'mengzi':
            print('gogogo')
        elif kwargs['name'] == 'laozi':
            print('nihao')
        else:
            print(kwargs)


if __name__ == '__main__':
    ins = ScCcWe()
    ins.get_random_article()

```
./test_use.py
```python
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# file_name: func_or_func().py
# author: ScCcWe
# time: 2020/3/26 20:11


from ScCcWe import ScCcWe


ScCcWe.get_random_article(name='zhuangzi')

```

## selenium
./base.py
```python
# encoding: utf-8
# !/user/bin/env python

import os
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


chromedriver = r"D:\hj\pycode\nihao\个人\chrome_driver\chromedriver.exe"


# 实例化一个浏览器
driver = webdriver.Chrome(executable_path=chromedriver)
# driver = webdriver.PhantomJS()

# 设置窗口大小
# driver.set_window_size(1920,1080)

# 最大化窗口
driver.maximize_window()

# 发送请求
driver.get("http://www.baidu.com")

driver.find_element_by_xpath('//*[@id="kw"]').send_keys('小猫')
driver.find_element_by_xpath('//*[@id="su"]').click()

```

## 删除列表中的空元素
### 第一种：
```python
while '' in test:
    test.remove('')
```
### 第二种：
```python
new_list_withour_0 = [i for i in test if i != '']
```

## 关于windows和linux中路径的转换
```python
if 'win' in sys.platform:
    path_route_format = '\\'
else:
    path_route_format = '/'
```
