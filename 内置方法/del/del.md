# python的垃圾回收机制
python的垃圾回收采用引用计数为主，标记清楚和分代收集两种机制为辅的策略。
## 1.引用计数机制
### 引用计数+1
    
    1.对象被创建  
    
        a=100  
    2.对象被引用  
    
        b=a  
    3.对象被作为参数，传到函数中  
        
        func(a)  
    4.对象作为一个元素，存储在容器中  
    
        list = [a, "dog", 2]  
    
### 引用计数-1
    
    1.当该对象的别名被显式销毁  
        
        del a  
    2.当该对象的别名被赋予新的对象  
        
        a=10  
    3.一个对象离开它的作用域，例如func函数执行完毕后，函数里面的局部变量的引用计数器就会减1(区别于全局变量，全局变量不会)  
    
    4.对象所在的容器被销毁或者对象从容器中删除  
    
        del list or list[1:]  
    
### 引用计数减1的2种情况：
    
    1.结果等于0  
    说明：1-1=0，销毁对象  
    2.结果大于0  
    说明：当使用del删除变量指向的对象时，如果对象的引用计数不为1，比如下面程序实例中的3，那么此时只会让这个引用计数减1，即变为2；
    当再次调用del时，变为1，如果再调用1次del，计数为0，,这时才会真的把对象进行删除。
    
### 程序实例：
```python
import time
   

class Animal(object):
    # 初始化方法
    # 创建完对象后会自动被调用
    def __init__(self, name):
        print('__init__方法被调用')
        self.__name = name
    
    # 析构方法
    # 析构函数 __del__ ，__del__在对象销毁的时候被调用，当对象不再被使用时，__del__方法运行：
    # 当对象被删除时，会自动被调用
    def __del__(self):
        print("__del__方法被调用")
        print("%s对象马上被干掉了..."%self.__name)


# 创建对象
dog = Animal("哈皮狗")

# 删除对象
del dog

cat = Animal("波斯猫")
cat2 = cat
cat3 = cat

print("---马上 删除cat对象")
del cat
print("---马上 删除cat2对象")
del cat2
print("---马上 删除cat3对象")
del cat3

print("程序2秒钟后结束")
time.sleep(2)
```
输出结果为：
```shell
__init__方法被调用
__del__方法被调用
哈皮狗对象马上被干掉了...
__init__方法被调用
---马上 删除cat对象
---马上 删除cat2对象
---马上 删除cat3对象
__del__方法被调用
波斯猫对象马上被干掉了...
程序2秒钟后结束
```
## 2.引用计数的优缺点
### 优点
1.简单  

2.实时性：一旦没有引用，内存就直接释放了，不用像其他机制等到特定时机。同时，实时性还带来了另一个好处：处理回收内存的时间分摊到了平时。
    
### 缺点
   
1.维护引用计数消耗资源  
2.循环引用
```python
a = []
b = []
b.append(a)
a.append(b)
del a
del b
```
说明：  
1.a与b相互引用，如果不存在其他对象对它们的引用，那么在del之后，a与b的引用计数也任然为1，所占用的内存永远无法被回收，这将是致命的。  
2.循环引用导致的内存泄漏，注定python还将引入新的回收机制。（标记清除和分代回收）

## 3.引用计数中C的身影
python里面的每一个东西都是对象，它们的核心就是一个结构体：PyObject
```
typedef struct _object {
_PyObject_HEAD_EXTRA
Py_ssize_t ob_refcnt;
struct _typeobject *ob_type;
} PyObject;
```
PyObject是每个对象必有的内容，其中ob_refcnt就是作为引用计数。当一个对象有新的引用时，它的ob_refcnt就会增加，当引用它的对象被删除，它的ob_refcnt就会减少
```
#define Py_INCREF(op) (                         \
_Py_INC_REFTOTAL  _Py_REF_DEBUG_COMMA       \
((PyObject *)(op))->ob_refcnt++)

#define Py_DECREF(op)                                   \
do {                                                \
    PyObject *_py_decref_tmp = (PyObject *)(op);    \
    if (_Py_DEC_REFTOTAL  _Py_REF_DEBUG_COMMA       \
    --(_py_decref_tmp)->ob_refcnt != 0)             \
        _Py_CHECK_REFCNT(_py_decref_tmp)            \
    else                                            \
        _Py_Dealloc(_py_decref_tmp);                \
} while (0)
```
当引用计数为0时，该对象生命就结束了。

### 4.何时会自动调用__del__方法?
- 删除所有的引用计数时，会自动调用
    ```python
    class Hero:
        def __del__(self):
            print("英雄已阵亡")
        
    man1 = Hero()
    man2 = man1
    del man1
    del man2
    print("程序执行完毕")
    ```
    输出结果为：  
    ```shell
    英雄已阵亡  
    程序执行完毕
    ```
    
- 未删除所有的引用计数，在程序结束之后调用
    ```python
    class Hero:
        def __del__(self):
            print("英雄已阵亡")
     
    man1 = Hero()
    man2 = man1
    del man1
    print("程序执行完毕")
    ```
    输出结果为：
    ```shell
    程序执行完毕  
    英雄已阵亡
    ```

## 2.标记清除  -------解决循环引用

## 3.分代回收
