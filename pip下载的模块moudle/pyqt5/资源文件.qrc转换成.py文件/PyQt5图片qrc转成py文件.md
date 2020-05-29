### 将图片资源转换成py文件

1.创建一个images.qrc文件，例如:
    
        <!DOCTYPE RCC>
        <RCC version="1.0">
        <qresource>
        <file alias="icons/delete.png">icons/delete.png</file>
        <file alias="icons/done.png">icons/done.png</file>
        <file alias="icons/edit.jpg">icons/edit.jpg</file>
        </qresource>
        </RCC>
        
2.输入命令(windows pycharm-terminal中)：

        $ pyrcc5 -o images.py images.qrc
        
### 使用这个images.py

        from images import *
        QIcon(":/icons/delete.png")
        
- 这里只需要注意调用路径的写法即可，不一定非要使用在QIcon中。
- 值得你十分注意的是，即便有有些时候 from images import * 显示是 unused ，也是不能删除这句导入的！
