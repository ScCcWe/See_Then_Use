# !/usr/bin/python
# -*- coding: utf-8 -*-
# file_name: origin_code.py
# function：None
# need_module: None
# author: ScCcWe
# time: 2020/1/15 11:35

import os
import sys
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from module.labelDialog import LabelDialog
from module.canvas import Canvas
from module.labelImgUi import Ui_MainWindow
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
# from images import *
import shutil


__appname__ = 'DisClass V1.0'


class MainWindow(QMainWindow, Ui_MainWindow):
    MODE_FIT_WINDOW, MODE_ADJUST_SIZE = ['F', 'A']
    
    def __init__(self):
        try:
            super(MainWindow, self).__init__()
            self.setupUi(self)
            self.setWindowTitle(__appname__)  # 标题
            self.setWindowIcon(QIcon(":/icons/pop.jpg"))
            
            self.mode = self.MODE_FIT_WINDOW
            self.father_path = None
            self.imgList = []
            self.imgQuantity = 0  # 图片数量
            self.imgShowNum = 0  # 图片位置，（在imgList列表中）
            
            # 改变按键的风格
            self.style_copy(self.toolButton_imgdir, 'open', '导入图片文件夹路径')
            self.style_copy(self.toolButton_nextImg, 'next', '下一张图片')
            self.style_copy(self.toolButton_preImg, 'prev', '上一张图片')
            self.style_copy(self.toolButton_zoom_in, 'zoom-in', '放大')
            self.style_copy(self.toolButton_zoom_out, 'zoom-out', '缩小')
            self.style_copy(self.toolButton_save_path, 'save-as', '更换保存路径')
            
            self.style_copy(self.toolButton_push_one, 'Burger', 'A类')
            self.style_copy(self.toolButton_push_two, 'Cup', 'B类')
            self.style_copy(self.toolButton_push_three, 'Chicken', 'C类')
            self.style_copy(self.toolButton_push_four, 'Grapes', 'D类')
            self.style_copy(self.toolButton_push_five, 'Fruits', 'E类')
            self.style_copy(self.toolButton_push_six, 'Lettuce', 'F类')
            self.style_copy(self.toolButton_push_seven, 'Wine', 'G类')
            self.style_copy(self.toolButton_push_eight, 'Rice', 'H类')
            self.style_copy(self.toolButton_push_nine, 'Steak', 'I类')
            self.style_copy(self.toolButton_push_ten, 'Strawberry', 'J类')
            self.style_copy(self.toolButton_push_eleven, 'Watermelon', 'K类')
            self.style_copy(self.toolButton_push_twelve, 'Soup', 'L类')
            
            self.style_copy(self.toolButton_one, 'Burger', '设定初始值')
            self.style_copy(self.toolButton_two, 'Cup', '设定初始值')
            self.style_copy(self.toolButton_three, 'Chicken', '设定初始值')
            self.style_copy(self.toolButton_four, 'Grapes', '设定初始值')
            self.style_copy(self.toolButton_five, 'Fruits', '设定初始值')
            self.style_copy(self.toolButton_six, 'Lettuce', '设定初始值')
            self.style_copy(self.toolButton_seven, 'Wine', '设定初始值')
            self.style_copy(self.toolButton_eight, 'Rice', '设定初始值')
            self.style_copy(self.toolButton_nine, 'Steak', '设定初始值')
            self.style_copy(self.toolButton_ten, 'Strawberry', '设定初始值')
            self.style_copy(self.toolButton_eleven, 'Watermelon', '设定初始值')
            self.style_copy(self.toolButton_twelve, 'Soup', '设定初始值')
            
            # 按键快捷键
            self.toolButton_preImg.setShortcut('A')
            self.toolButton_nextImg.setShortcut('D')
            self.toolButton_zoom_in.setShortcut('Space')
            self.toolButton_push_one.setShortcut('1')
            self.toolButton_push_two.setShortcut('2')
            self.toolButton_push_three.setShortcut('3')
            self.toolButton_push_four.setShortcut('4')
            self.toolButton_push_five.setShortcut('5')
            self.toolButton_push_six.setShortcut('6')
            self.toolButton_push_seven.setShortcut('7')
            self.toolButton_push_eight.setShortcut('8')
            self.toolButton_push_nine.setShortcut('9')
            self.toolButton_push_ten.setShortcut('0')
            self.toolButton_push_eleven.setShortcut('-')
            self.toolButton_push_twelve.setShortcut('=')
            
            # 画布控件
            self.canvas = Canvas(parent=self)
            self.scrollArea.setWidget(self.canvas)
            self.scrollArea.setWidgetResizable(True)
            
            # self.listWidget_filenames.itemDoubleClicked.connect(self.file_item_double_clicked)
            
            self.jsonPathList = []
            
            self.dirty_png = False
            self.dirty_jpg = False
            
            self.labelHist = None
            
            self.label_dialog = LabelDialog(parent=self, listItem=self.labelHist)
            self.prevLabelText = ''
            self.label_one = ''
            self.label_two = ''
            self.label_three = ''
            self.label_four = ''
            self.label_five = ''
            self.label_six = ''
            self.label_seven = ''
            self.label_eight = ''
            self.label_nine = ''
            self.label_ten = ''
            self.label_eleven = ''
            self.label_twelve = ''
            
            self.save_path = None
            
        except Exception as e:
            print('Error in init:', e)
    
    def pre_img(self):
        if 0 < (self.imgShowNum + 1) - 1:
            self.mode = self.MODE_FIT_WINDOW
            
            self.imgShowNum -= 1
            self.label_all_img.setText('图片总数：' + str(self.imgShowNum + 1) + '/' + str(self.imgQuantity))
            self.label_cur_img.setText("当前图片: " + self.imgList[self.imgShowNum + 1])
            
            pre_img_path = self.father_path + '/' + self.imgList[self.imgShowNum]
            
            self.canvas_show_sth(pre_img_path)
            
            pre_img_json_path = self.father_path + '//' + 'tempJson' + '//' + \
                                self.imgList[self.imgShowNum].split('.', 2)[0] + '.json'
            if os.path.exists(pre_img_json_path):
                self.load_json_file(pre_img_json_path)
        else:
            QMessageBox.warning(
                self,
                'WARNING',
                '不能再往前拉！！！',
                QMessageBox.Yes | QMessageBox.No,  # 两个选项
                QMessageBox.Yes  # 加重凸显
            )
    
    def next_img(self):
        try:
            # (self.imgShowNum + 1) 实际数量
            if (self.imgShowNum + 1) + 1 <= self.imgQuantity:  # imgShowNum从0开始，img+1是它的实际数量
                self.mode = self.MODE_FIT_WINDOW
                # 提供一些下一张和上一张的交互
                self.imgShowNum += 1
                self.label_all_img.setText('图片总数：' + str(self.imgShowNum + 1) + '/' + str(self.imgQuantity))
                self.label_cur_img.setText("当前图片: " + self.imgList[self.imgShowNum + 1])
                
                next_img_path = self.father_path + '/' + self.imgList[self.imgShowNum]
                self.canvas_show_sth(next_img_path)
                
                next_img_json_path = self.father_path + '//' + 'tempJson' + '//' + \
                                     self.imgList[self.imgShowNum].split('.', 2)[0] + '.json'
                if os.path.exists(next_img_json_path):
                    self.load_json_file(next_img_json_path)
            else:
                QMessageBox.warning(
                    self,
                    'WARNING',
                    '不能再往后拉！！！',
                    QMessageBox.Yes | QMessageBox.No,
                    QMessageBox.Yes)
        except Exception as e:
            print('Error in next:', e)
    
    @staticmethod
    def style_copy(button, name, introduce_text):
        button.setIcon(QIcon(":/icons/" + name + ".png"))
        button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        button.setAutoRaise(True)
        # button.setStyleSheet("border:none;")
        button.setToolTip(introduce_text)
    
    def load_img_dir(self):
        try:
            self.father_path = QFileDialog.getExistingDirectory(self, '选择打开的目录')
            if self.father_path == '':
                QMessageBox.warning(
                    self,
                    'WARNING',
                    '没有选择一个正确的路径！',
                    QMessageBox.Yes | QMessageBox.No,
                    QMessageBox.Yes)
            else:
                if self.save_path is None:
                    self.save_path = self.father_path
                self.label_savePath.setText('当前保存路径为：' + self.save_path)
                # get a list only have img
                fileList = os.listdir(self.father_path)
                for i in range(len(fileList)):
                    # the same as split('.', find_person)[1]
                    temp = fileList[i].split('.')[-1]
                    if temp in ['jpg', 'png', 'jpeg', 'JPG', 'PNG', 'JPEG']:
                        self.imgList.append(fileList[i])
                
                if self.imgList:
                    import natsort
                    self.imgList = natsort.natsorted(self.imgList)
                    
                    self.imgQuantity = len(self.imgList)
                    self.label_all_img.setText('图片总数：' + str(self.imgShowNum + 1) + '/' + str(self.imgQuantity))
                    self.imgShowNum = 0
                    self.label_cur_img.setText("当前图片: " + self.imgList[self.imgShowNum])
                    
                    current_img_path = self.father_path + '/' + self.imgList[self.imgShowNum]
                    current_json_path = self.father_path + '//' + 'tempJson' + '//' + \
                                        self.imgList[self.imgShowNum].split('.', 2)[0] + '.json'
                    
                    self.canvas_show_sth(current_img_path)
                    
                    if os.path.exists(current_json_path):
                        self.load_json_file(current_json_path)
        except Exception as e:
            print(e)
    
    def file_or_dir_fit_window(self):
        if self.mode == self.MODE_FIT_WINDOW:
            self.canvas.scale = self.scale_fit_window()  # 随之变动
            self.canvas.adjustSize()
            self.update()
        elif self.mode == self.MODE_ADJUST_SIZE:
            self.canvas.adjustSize()
            self.update()
    
    def canvas_show_sth(self, imagepath):
        """画布展示img"""
        try:
            self.dirty_jpg = False
            self.dirty_png = False
            # imagepath = r'D:\task\300\0300_310.jpg'
            # print(imagepath)
            # print(imagepath.split('.')[-1])
            # print(imagepath.split('/')[-1].split('.')[0])
            self.pic_without_format_name = imagepath.split('/')[-1].split('.')[0]
            # print(self.father_path)
            
            from PIL import Image
            ends_with_format_word = imagepath.split('.')[-1]
            img = Image.open(imagepath)
            # print(img.format.lower())
            img_format_lower_bottle = img.format.lower()
            if img_format_lower_bottle == 'jpeg' and ends_with_format_word != 'jpg':
                img.save(self.father_path + '//' + self.pic_without_format_name + '.jpg')
                imagepath = self.father_path + '//' + self.pic_without_format_name + '.jpg'
                self.dirty_jpg = True
            if img_format_lower_bottle == 'png' and ends_with_format_word != 'png':
                img.save(self.father_path + '//' + self.pic_without_format_name + '.png')
                imagepath = self.father_path + '//' + self.pic_without_format_name + '.png'
                self.dirty_png = True
            
            image = QImage(imagepath)
            # print(image)
            self.canvas.load_pixmap(QPixmap.fromImage(image))
            # print(self.canvas.pixmap.width())
            # print()
            
            # canvas fit window
            print('self.scale_fit_window():', self.scale_fit_window())
            self.file_or_dir_fit_window()
            
            self.delete_dirty_pic()
        except Exception as e:
            print('Error in canvas_show_sth:', e)
    
    @staticmethod
    def mk_dirs(parameter_path):
        if not os.path.exists(parameter_path):
            os.makedirs(parameter_path)
    
    def scale_fit_window(self):
        """
        功能：
            返回一个小于1的比例，这样进来的图片永远不会大于边框，而且只要乘上比例，就可以保持比例
        实现：
            根据像素图的宽高比计算新的比例值。
            如果进来的图片宽高比大于原来的框，类似于右边多出一块，这时 w1/w2 小于0
            反之h1/h2 小于0 这样子，加入的图就不会大过于框。而且会保持比例(只需乘上比例即可)
        """
        e = 2.0  # So that no scrollbars are generated.
        w1 = self.scrollArea.width() - e
        h1 = self.scrollArea.height() - e
        a1 = w1 / h1  # 宽高比a1  例如：16:9
        w2 = self.canvas.pixmap.width() - 0.0
        h2 = self.canvas.pixmap.height() - 0.0
        a2 = w2 / h2
        return w1 / w2 if a2 >= a1 else h1 / h2
    
    def delete_dirty_pic(self):
        if self.dirty_png:
            os.remove(self.seleDir + '//' + self.pic_without_format_name + '.png')
        if self.dirty_jpg:
            os.remove(self.seleDir + '//' + self.pic_without_format_name + '.jpg')
    
    def add_zoom(self):
        self.mode = self.MODE_ADJUST_SIZE
        self.canvas_show_sth(os.path.join(self.father_path, self.imgList[self.imgShowNum]))
        self.canvas.scale *= 1.1  # 随之变动
        self.canvas.adjustSize()
        # print(self.canvas.size())  # 缩放的关键点
        self.canvas.update()
    
    def subtract_zoom(self):
        self.mode = self.MODE_ADJUST_SIZE
        self.canvas_show_sth(os.path.join(self.father_path, self.imgList[self.imgShowNum]))
        self.canvas.scale *= 0.9  # 随之变动
        self.canvas.adjustSize()
        self.canvas.update()
    
    def input_save_path(self):
        new_save_path = QFileDialog.getExistingDirectory(self, '指定一个保存路径')
        if new_save_path == '':
            QMessageBox.warning(
                self,
                'WARNING',
                '没有选择一个正确的路径!',
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.Yes)
        else:
            self.save_path = new_save_path
            self.label_savePath.setText('当前保存路径: ' + self.save_path)
            # print(self.save_path)
    
    """这里并没有能实现一个函数"""
    
    def input_one(self):
        self.label_one = self.label_dialog.popUp(text=self.prevLabelText)
        if self.label_one:
            self.toolButton_one.setText(self.label_one)
    
    def input_two(self):
        self.label_two = self.label_dialog.popUp(text=self.prevLabelText)
        if self.label_two:
            self.toolButton_two.setText(self.label_two)
    
    def input_three(self):
        self.label_three = self.label_dialog.popUp(text=self.prevLabelText)
        if self.label_three:
            self.toolButton_three.setText(self.label_three)
    
    def input_four(self):
        self.label_four = self.label_dialog.popUp(text=self.prevLabelText)
        if self.label_four:
            self.toolButton_four.setText(self.label_four)
    
    def input_five(self):
        self.label_five = self.label_dialog.popUp(text=self.prevLabelText)
        if self.label_five:
            self.toolButton_five.setText(self.label_five)
            
    def input_six(self):
        self.label_six = self.label_dialog.popUp(text=self.prevLabelText)
        if self.label_six:
            self.toolButton_six.setText(self.label_six)
    
    def input_seven(self):
        self.label_seven = self.label_dialog.popUp(text=self.prevLabelText)
        if self.label_seven:
            self.toolButton_seven.setText(self.label_seven)
    
    def input_eight(self):
        self.label_eight = self.label_dialog.popUp(text=self.prevLabelText)
        if self.label_eight:
            self.toolButton_eight.setText(self.label_eight)
    
    def input_nine(self):
        self.label_nine = self.label_dialog.popUp(text=self.prevLabelText)
        if self.label_nine:
            self.toolButton_nine.setText(self.label_nine)
    
    def input_ten(self):
        self.label_ten = self.label_dialog.popUp(text=self.prevLabelText)
        if self.label_ten:
            self.toolButton_ten.setText(self.label_ten)
    
    def input_eleven(self):
        self.label_eleven = self.label_dialog.popUp(text=self.prevLabelText)
        if self.label_eleven:
            self.toolButton_eleven.setText(self.label_eleven)
    
    def input_twelve(self):
        self.label_twelve = self.label_dialog.popUp(text=self.prevLabelText)
        if self.label_twelve:
            self.toolButton_twelve.setText(self.label_twelve)
    
    def move_this(self, label_data):
        try:
            if label_data:
                self.mk_dirs(self.save_path)
                new_parent_path = os.path.join(self.save_path, label_data)
                self.mk_dirs(new_parent_path)
                old_path = os.path.join(self.father_path, self.imgList[self.imgShowNum])
                shutil.move(old_path, os.path.join(new_parent_path, self.imgList[self.imgShowNum]))
                self.next_img()
        except Exception as e:
            print('Error in move', e)
    
    def move_one(self):
        self.move_this(self.label_one)
    
    def move_two(self):
        self.move_this(self.label_two)
    
    def move_three(self):
        self.move_this(self.label_three)
    
    def move_four(self):
        self.move_this(self.label_four)
    
    def move_five(self):
        self.move_this(self.label_five)
    
    def move_six(self):
        self.move_this(self.label_six)
    
    def move_seven(self):
        self.move_this(self.label_seven)
    
    def move_eight(self):
        self.move_this(self.label_eight)
    
    def move_nine(self):
        self.move_this(self.label_nine)
    
    def move_ten(self):
        self.move_this(self.label_ten)
    
    def move_eleven(self):
        self.move_this(self.label_eleven)
    
    def move_twelve(self):
        self.move_this(self.label_twelve)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
