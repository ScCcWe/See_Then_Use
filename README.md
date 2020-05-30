# See Then Use

## 即看即用

包含了一系列的python代码，有各种内置库和pip库。希望看到本项目的人，可以找到需要的示例...

## 总览

`内置方法和库:`
- [数据的存储和读取-json](https://github.com/ScCcWe/See_Then_Use/blob/master/%E5%86%85%E7%BD%AE%E6%96%B9%E6%B3%95/json/json.md)
- [多线程-threading](https://github.com/ScCcWe/See_Then_Use/blob/master/%E5%86%85%E7%BD%AE%E6%96%B9%E6%B3%95/%E5%A4%9A%E7%BA%BF%E7%A8%8B/threading_demo.py)
- [多进程-multiprocessing](https://github.com/ScCcWe/See_Then_Use/blob/master/%E5%86%85%E7%BD%AE%E6%96%B9%E6%B3%95/%E5%A4%9A%E8%BF%9B%E7%A8%8B/%E5%A4%9A%E8%BF%9B%E7%A8%8B/demo.py)  
- [断言-assert](https://github.com/ScCcWe/See_Then_Use/blob/master/%E5%86%85%E7%BD%AE%E6%96%B9%E6%B3%95/%E6%96%AD%E8%A8%80assert/assert.md)
- [日志-logging](https://github.com/ScCcWe/See_Then_Use/blob/master/%E5%86%85%E7%BD%AE%E6%96%B9%E6%B3%95/log/use_log.py)
- [属性操作-getattr-hasattr-setattr](https://github.com/ScCcWe/See_Then_Use/blob/master/%E5%86%85%E7%BD%AE%E6%96%B9%E6%B3%95/%E6%9C%89%E5%85%B3%E5%B1%9E%E6%80%A7%E7%9A%84%E6%96%B9%E6%B3%95attr/hassttr.md)
- [del](https://github.com/ScCcWe/See_Then_Use/blob/master/%E5%86%85%E7%BD%AE%E6%96%B9%E6%B3%95/del/del.md)  

`pip库:`
- [自然排序-natsort](https://github.com/ScCcWe/See_Then_Use/blob/master/pip%E4%B8%8B%E8%BD%BD%E7%9A%84%E6%A8%A1%E5%9D%97moudle/%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%8E%92%E5%BA%8F/%E8%87%AA%E7%84%B6%E6%8E%92%E5%BA%8F.md)
- [虚拟数据-faker](https://github.com/ScCcWe/See_Then_Use/tree/master/pip%E4%B8%8B%E8%BD%BD%E7%9A%84%E6%A8%A1%E5%9D%97moudle/%E7%94%9F%E6%88%90%E8%99%9A%E6%8B%9F%E6%95%B0%E6%8D%AE)
- [自动代码格式-autopep8](https://github.com/ScCcWe/See_Then_Use/blob/master/pip%E4%B8%8B%E8%BD%BD%E7%9A%84%E6%A8%A1%E5%9D%97moudle/autopep8/autopep8.md)
- [程序监控-tqdm](https://github.com/ScCcWe/See_Then_Use/blob/master/pip%E4%B8%8B%E8%BD%BD%E7%9A%84%E6%A8%A1%E5%9D%97moudle/%E7%A8%8B%E5%BA%8F%E7%9B%91%E6%8E%A7/tqdm_use.md)
- [GUI编程-pyqt5](https://github.com/ScCcWe/See_Then_Use/tree/master/pip%E4%B8%8B%E8%BD%BD%E7%9A%84%E6%A8%A1%E5%9D%97moudle/pyqt5)
- [GUI编程工具例-labelsix](https://github.com/ScCcWe/See_Then_Use/tree/master/pip%E4%B8%8B%E8%BD%BD%E7%9A%84%E6%A8%A1%E5%9D%97moudle/pyqt5/labelsix)
- [图片处理-pillow](https://github.com/ScCcWe/See_Then_Use/blob/master/pip%E4%B8%8B%E8%BD%BD%E7%9A%84%E6%A8%A1%E5%9D%97moudle/%E5%88%B6%E4%BD%9Cico%E5%9B%BE%E6%A0%87/make_ico.md)  
- [输出着色-colorama](https://github.com/ScCcWe/See_Then_Use/blob/master/pip%E4%B8%8B%E8%BD%BD%E7%9A%84%E6%A8%A1%E5%9D%97moudle/colorama/use.py)  

`数据结构`
- [python环境搭建](https://github.com/ScCcWe/See_Then_Use/tree/master/data_structure)

`《流畅的python》读书笔记：`
- [装饰器](https://github.com/ScCcWe/See_Then_Use/blob/master/%E6%B5%81%E7%95%85%E7%9A%84python%E8%AF%BB%E4%B9%A6%E8%AE%B0%E5%BD%95/%E8%A3%85%E9%A5%B0%E5%99%A8.md)
- [一切皆是对象](https://github.com/ScCcWe/See_Then_Use/blob/master/%E6%B5%81%E7%95%85%E7%9A%84python%E8%AF%BB%E4%B9%A6%E8%AE%B0%E5%BD%95/%E4%B8%80%E5%88%87%E7%9A%86%E6%98%AF%E5%AF%B9%E8%B1%A1.md)

`新手`
- [python环境搭建](https://github.com/ScCcWe/See_Then_Use/blob/master/before_code/01_before_code/beforeCode.md)

## what is life
```python
def what_is_life(want, life):
    for year, get in enumerate(life):
        if get in want:
            return
        continue
```
