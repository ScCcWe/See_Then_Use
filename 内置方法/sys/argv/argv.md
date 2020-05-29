### 源码中经常出现的argv，形如django源码中出现的一段代码：
- 代码展示
    
    ```python
        ...
        def __init__(self, argv=None):
            self.argv = argv or sys.argv[:]
            ...
        ...
    ```

### 解释
- sys.argv是一个可以提供外部参数的东西，见如下代码

    ```python
    # !/usr/bin/env python
    # -*- coding: utf-8 -*-
    # file_name: test_use.py
    # author: ScCcWe
    # time: 2020/3/24 19:37
    import sys
    
    
    # print(sys.argv)
    # print(sys.argv[0])
    # print(sys.argv[:])
    
    # print(sys.argv[1])
    if sys.argv[1] == 'startproject':
        print('success')
    ```
- 在终端中输入下述命令以运行上述代码

    ```shell
    $ python test_use.py startproject
    ```

    可以看到输出结果为`success`，这是因为因为程序接收了外部参数`startproject`。
    
### 应用
- 初步

    可以将其写入自己的框架中，以实现类似于django命令行实现程序包的功能。
