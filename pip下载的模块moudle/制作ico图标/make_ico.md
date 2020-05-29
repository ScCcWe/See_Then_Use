### 1.下载需要的模块：
- 从pip下载
```bash
$ pip install pillow
```
- 如果下载速度太慢，或者下载失败了。试试下面这个命令吧：
```bash
$ pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pillow
```
### 2.转换图片格式：

- 将一张狗的图片dog.jpg转换为dog.png：
```python
from PIL import Image

img = Image.open('dog.jpg')
img.save('dog.png')
```
- 制作一个狗的图标dog.ico，类似于：`img.save('dog.ico')` , 并且一般ico的大小是32x32左右，代码如下：
```python
from PIL import Image
   
img = Image.open('dog.jpg')
   
print(img.format)
print(img.mode)
print(img.size)
   
img_resize = img.resize((32, 32))
img_resize.save('test_2.ico')
```
