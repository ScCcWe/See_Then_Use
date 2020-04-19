# 配置环境

## win

- python的下载和安装

    去[官网下载](https://www.python.org/downloads/)安装包。打开安装包，如果不想麻烦，一直点下一步即可。当然，我个人喜欢把python安装在D盘一个可以找到的路径中，所以我会修改一下安装路径。

- IDE(集成开发工具)的选择

    我个人建议初学者也该直接使用`pycharm`来编写代码。为什么？因为`pycharm`足够好，也足够方便易用。
    
    同时下面的设置或者配置都是基于`pycharm`实现的，当然，你可以选择自己喜欢的IDE，随你好了。
    
    同样的，去[官网下载](https://www.jetbrains.com/pycharm/download/#section=windows)安装包，选择community版本即可。我个人是不建议直接购买Professional版本的，同样的，我也不建议你去使用破解版本，一是因为破解起来太浪费时间，二是没有必要，初学者需要的功能，community版本是全部都有的。
- 在pycharm中配置python环境

    左上角`file`->`settings`->`project:...`->`project Interpreter`，将需要的路径设置成你的python路径。可能是设置好的，你需要动用自己发达的视力查看一下。
    
## 完成了上述的步骤，就可以开始写python代码了

## 下面是一些拓展的部分，你可以试着先`star`本教程, 也许你以后会用到 :)

### 在pycharm中使用虚拟环境

- 写在之前

    为什么使用虚拟环境？你肯定有这个疑问。
    对于有这样疑问的人，最好的办法是先star本教程，不要使用虚拟环境，遇到问题的时候在来看看吧

- 配置

    左上角`file`->`settings`->`project:...`->`project Interpreter`, 接着点击右上角的小齿轮，在点击`Add...`
    看到出来的界面，将`New environment`前面的小圆圈点上
    然后在下面的`Base interpreter`中选择上自己的python安装路径(即python.exe的路径)
    完成上述步骤后，点击ok，等待虚拟环境的载入。
    
### 配置一个国内的`pip`源

- 配置之前

    (初学者无需使用pip安装模块，所以是感受不到好处的。建议可以先star本教程，在你学习完python基础之后在来看。)
    
    在配置之前，先感受一下乌龟的速度，`pip install flask`
    
    是不是根本下载不动呢？当然了，因为网络有限制。这时候，按下`Ctrl+C`，取消安装
    
- 正式配置
    
    找到用户文件夹(一般`windows`都是在`C盘`下的`用户`目录里面)
    在里面新建一个pip文件夹，在pip文件夹中新建一个pip.ini，输入下面的内容
    ```
    [global]
    trusted-host=rnd-mirrors.huawei.com
    index-url=http://rnd-mirrors.huawei.com/pypi/simple/
    ```
    现在在使用`pip install flask`感受一下安装速度
    
    
### 使用`git`来管理代码

        $ git init
        
