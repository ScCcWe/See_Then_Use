# 关于 json 的读和写
## 01.写和读的入门
### 写入json
- 直接写
    ```python
    import json
    
    data = {
        "name": "小狗",
        "age": 12
    }
    # 'w' 模式可写，且覆盖写
    with open('./one.json', 'w', encoding='utf-8') as f:
        # json.dump(data, f, indent=4, ensure_ascii=False)  # indent=4可以不加，加上去的话json格式会好看一些
        f.write(json.dumps(data, ensure_ascii=False, indent=4))  # 完全同上
    ```
    结果：创建了一个用于下面代码的**one.json**文件, 如果是在 pycharm 中创建的，可以直接双击打开**one.json**看一看。
   
### 读取json
- 最简便的读取
    ```python
    import json
    
    # './one.json'表示同级目录下的 one.json
    with open('./one.json', 'r', encoding='utf-8') as f: # 'r' 模式只能读
        data = json.load(f)
        print(data)
    ```
    结果：读取了刚才创建的**one.json**, 可以自行观察输出。
    
## 02.写和读的用法举例

### 读取和写入的同时使用

- 先读取再写入

    ```python
    import json

    with open('./one.json', 'r', encoding='utf-8') as f:  
        data = json.load(f)
    
    # 'w+' 模式可读可写，且覆盖写；所以其实使用 'w' 或者 'W+' 都是可以的。随你喜欢吧。
    with open('./two.json', 'w+', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)  
    ```
    
    结果：将读取的data写入到**two.json**
    
- 先读取，读取完之后做一些简单的处理，再写入
    ```python
    import json

    with open('./one.json', 'r', encoding='utf-8') as f:  
        data = json.load(f)
        print(data)
        # 输出读取的 json 数据的 key 值
        print(data.keys())
        # 将data数据的 age 字段删除，供下面的写入使用
        if 'age' in data.keys():
            data.pop('age')

    with open('./three.json', 'w+', encoding='utf-8') as f:    
        f.write(json.dumps(data, ensure_ascii=False, indent=4))  
    ```
    结果：将处理完的data写入了一个新的json文件**three.json**，当然，真实的数据操作要比这复杂的多，在那时，还需要你多多开动聪明的脑袋。
    
## 03.不该出现在这里的东西(在 json 文件读写时常用的方法)

### 文件夹相关

- 新建文件夹
    ```python
    def mkdir_P(path):
        if not os.path.exists(path):
            os.makedirs(path)
    ```
    方法名是不是很眼熟呢？没错，类似于linux中的`mkdir -p`，功能也很类似，mkdir_p('./test_use/hello/') 表示在当前路径下新建了test_use文件夹，在test_use文件夹下新建了hello文件夹。
    
### 多进程，多线程的加速
- [多进程模板](https://github.com/ScCcWe/See_Then_Use/blob/master/%E5%BA%93%E7%9B%B8%E5%85%B3/%E5%A4%9A%E8%BF%9B%E7%A8%8B/mul_process.py)
- [多线程模板](https://github.com/ScCcWe/See_Then_Use/blob/master/%E5%BA%93%E7%9B%B8%E5%85%B3/%E5%A4%9A%E7%BA%BF%E7%A8%8B/threading_demo.py)  
    个人建议使用多进程。当然，不使用多线程或者多进程完全也可以。但是，当操作太多数据的时候(比如脚本跑几天都跑不完)，你应该考虑一下使用多进程。  
    需要记住的是：多进程，多线程不是必要的！当你的代码中功能逻辑都不是很清晰的时候，就完全没必要使用多进程，多线程了！
