# 关于图片的格式问题

### 1.问题描述：

在实际应用中，在图片的格式上往往会遇到一些意想不到的问题。 

例如，明明我这里可以显示`这种格式`的图片，他给的`这种格式`的图片怎么就不能显示呢？

这里可以把问题简化为图片格式(format)的`判断`与`转换`。

### 2.解决方案：

- 首先判断图片的`真实`格式，代码如下:  
./pic_show.py
```python
from PIL import Image


img = Image.open(r'D:\icons\test.png')

print(img.format)
print(img.mode)
print(img.size)
```

输出的结果为：
```bash
$ python pic_show.py
JPEG
RGB
(4608, 3456)
```
可以看到，test.png的`真实`格式是JPEG，而不是所谓的PNG。

- 接下来对图片的格式进行转换，代码如下：
```python
from PIL import Image


img = Image.open(r'D:\icons\test.png')

img.save(r'D:\icons\test.jpg')
```
### 3.实际应用：

上面只是简单的介绍了解决的方法，实际的使用又是怎么样的呢？

- 这里举一个pyqt5中的QPixmap获取图片的例子，代码如下：

```python
imagepath = r'D:\icons\test.jpg'
image = QImage(imagepath)
pixmap_obj = QPixmap.fromImage(image)
```

- 正常使用时，就如上面所示。而实际使用时，则需要下面这样：

```python
imagepath = 'D://icons//test.jpg
img_type = imagepath.split('.')[-1]  # jpg
img_name = imagepath.split('//')[-1].split('.')[0]  # test

from PIL import Image
img = Image.open(imagepath)
print(img.format.lower())
img_true_type = img.format.lower()
            
if img_ture_type == 'jepg' and img_type != 'jpg':
    img.save('D://icons//' + img_name + '.jpg')
    imagepath = 'D://icons//' + img_name + '.jpg'
if img_true_type == 'png' and img_type != 'png':
    img.save('D://icons//' + img_name + '.png')
    imagepath = 'D://icons//' + img_name + '.png'

image = QImage(imagepath)
pixmap_img = QPixmap.fromImage(image)
```

因为我们需要的数据源并不总是可靠的，所以在读取图片的时候，需要增加一个判断。

如上述代码所述，当遇到后缀为.jpg的图片，但实际格式为png的图片时，我们先保存一张符合真实格式的图片(如: 通过test.jpg得到test.png)。

- 实际使用中，基本都是类方法，同时，在这里我们还可以增加一个删除方法，增加一个判断条件，使得看见可以和删除'同时发生'：

```python
# 忽略需要定义的类, 要实现代码功能还需要你自己定义类！
# 这里只取两个实际应用中的方法，来展示一下！
def delete_dirty_pic(self):
    if self.dirty_png:
        os.remove('D://icons//' + img_name + '.png')
    if self.dirty_jpg:
        os.remove('D://icons//' + img_name + '.jpg')

def canvas_show_img(self):
    imagepath = 'D://icons//test.jpg
    img_type = imagepath.split('.')[-1]  # jpg
    img_name = imagepath.split('//')[-1].split('.')[0]  # test

    from PIL import Image
    img = Image.open(imagepath)
    print(img.format.lower())
    img_true_type = img.format.lower()

    if img_ture_type == 'jepg' and img_type != 'jpg':
        img.save('D://icons//' + img_name + '.jpg')
        imagepath = 'D://icons//' + img_name + '.jpg'
        self.dirty_jpg = True
    if img_true_type == 'png' and img_type != 'png':
        img.save('D://icons//' + img_name + '.png')
        imagepath = 'D://icons//' + img_name + '.png'
        self.dirty_png = False

    image = QImage(imagepath)
    self.canvas.load_pixmap(QPixmap.fromImage(image))  # 这里的self.cavas也是需要自己定义的类，一个画布
    
    self.delete_dirty_pic()
```

使用 self.dirty_png 和 self.dirty_jpg 作为判断条件，定义了一个delete_dirty_pic()方法，使得看见和删除可以`同时`发生。是不是很酷呢！

如此一来，就可以解决这个问题了。

### 4.不足之处：

虽然问题解决了，但是程序性能会受到一定的影响，好在这种错误发生的概率不大。所以在实际使用中，操作人员应该是不会感受到的。╮(╯▽╰)╭
