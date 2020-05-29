# !/usr/bin/env python
# -*- coding: utf-8 -*-
# file_name: labelimg_six.py
# author: ScCcWe
# time: 2020/4/23 9:29
"""
框选 + 标记工具，框选借鉴labelimg，标记自己搭建
"""
import os
import sys

if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']

import copy
import json
from natsort import natsorted
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from UI_six import Ui_MainWindow
from libs.canvas import Canvas
from libs.shape import Shape
from images import *

__appname__ = 'label_SIX'
FORMAT_DICT_DICT_LIST = {'backlight': ['yes', 'no'],
                         'hasGlove': ['yes', 'no'],
                         'resolution': ['clear', 'blur', 'dark', 'invisible'],
                         'immerse': ['yes', 'no'],
                         'lightOn': ['on', 'off'],
                         'integrity': ['full', '80%+', '80%-', 'nodevice'],
                         'angle': ['front', 'side']}
FORMAT_DICT_KEY_LIST = ['backlight', 'hasGlove', 'resolution', 'immerse', 'lightOn', 'integrity', 'angle']
FORMAT_DICT_DEFAULT = {FORMAT_DICT_KEY_LIST[0]: 'no',
                       FORMAT_DICT_KEY_LIST[1]: 'no',
                       FORMAT_DICT_KEY_LIST[2]: 'clear',
                       FORMAT_DICT_KEY_LIST[3]: 'no',
                       FORMAT_DICT_KEY_LIST[4]: 'on',
                       FORMAT_DICT_KEY_LIST[5]: 'full',
                       FORMAT_DICT_KEY_LIST[6]: 'front'}


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    CREATE, EDIT = list(range(2))
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        __appicon__ = QtGui.QIcon(":/icons/" + 'pipi.jpg')
        self.setWindowIcon(__appicon__)            # 设置主程序图标
        self.setWindowTitle(__appname__)           # 设置主程序标题
        self.dir_list = None                       # 文件列表(打开的全部)
        self.dir_quantity = 0                      # 文件总数
        self.seleDir = None                        # 文件父路径
        self.dir_show_num = 0                      # 当前文件的index
        
        self.exampleDict = self.set_format_dict()  # 标注字典格式
        self.tempDict = None                       # 实际使用的字典壳子，通过深拷贝(copy.deepcopy())
        
        self.set_button_icons()                    # 设置按钮的图标
        self.init_button_setting()                 # 初始化按钮的设置
        
        self.button_list = [self.pushButton_backlight_yes,
                            self.pushButton_backlight_no,
                            self.pushButton_hasGlove_yes,
                            self.pushButton_hasGlove_no,
                            self.pushButton_resolution_clear,
                            self.pushButton_resolution_blur,
                            self.pushButton_resolution_dark,
                            self.pushButton_resolution_invisible,
                            self.pushButton_immerse_yes,
                            self.pushButton_immerse_no,
                            self.pushButton_lightOn_on,
                            self.pushButton_lightOn_off,
                            self.pushButton_integrity_full,
                            self.pushButton_integrity_complete,
                            self.pushButton_integrity_incomplete,
                            self.pushButton_integrity_nodevice,
                            self.pushButton_angle_front,
                            self.pushButton_angle_side]
        
        self._noSelectionSlot = False
        
        self.listWidget.itemDoubleClicked.connect(self.fileitemDoubleClicked)
        
        self.canvas = Canvas()
        self.cursor = self.canvas.cursor
        self.scrollArea.setWidget(self.canvas)
        # self.canvas.scrollRequest.connect(self.scrollRequest)
        self.canvas.newShape.connect(self.newShape)
        # self.canvas.shapeMoved.connect(self.setDirty)
        self.canvas.selectionChanged.connect(self.shapeSelectionChanged)
        # self.canvas.drawingPolygon.connect(self.toggleDrawingSensitive)
        
        # 初始化时就设置自动保存
        self.action_autosave.setCheckable(True)
        self.action_autosave.setChecked(True)
    
    @staticmethod
    def set_format_dict():
        # 得到一个标注格式的字典壳子
        a = {}
        for i in FORMAT_DICT_KEY_LIST:
            a[i] = ''
        return a
    
    def set_button_icons(self):
        self.action_root.setIcon(QtGui.QIcon(":/icons/open.png"))
        self.action_pre.setIcon(QtGui.QIcon(":/icons/prev.png"))
        self.action_next.setIcon(QtGui.QIcon(":/icons/next.png"))
        self.action_edit.setIcon(QtGui.QIcon(":/icons/edit.png"))
        self.action_rect.setIcon(QtGui.QIcon(":/icons/objects.png"))
        self.action_save.setIcon(QtGui.QIcon(":/icons/save.png"))
        self.action_delete.setIcon(QtGui.QIcon(":/icons/delete.png"))
        self.action_autosave.setIcon(QtGui.QIcon(":/icons/done.png"))
        self.action_copy.setIcon(QtGui.QIcon(":/icons/copy.png"))
    
    def init_button_setting(self):
        self.action_next.setEnabled(False)
        self.action_pre.setEnabled(False)
        self.action_save.setEnabled(False)
        self.action_rect.setEnabled(False)
        self.action_edit.setEnabled(False)
        self.action_delete.setEnabled(False)
        self.action_copy.setEnabled(False)
    
    def init_button_func(self):
        self.action_next.setEnabled(True)
        self.action_pre.setEnabled(True)
        self.action_save.setEnabled(True)
        self.action_rect.setEnabled(True)
    
    def deleteSelectedShape(self):
        shape = self.canvas.deleteSelected()
        if shape:
            self.init_color()
        self.action_edit.setEnabled(False)
        self.action_delete.setEnabled(False)
    
    # React to canvas signals. (对画布信号做出反应)
    # 具体反应在list中, 还有rect本身
    def shapeSelectionChanged(self, selected=False):
        if self._noSelectionSlot:  # 如果用户没有选择rect(初始值即为False), 将re（这是防止出现错误）
            self._noSelectionSlot = False
        else:
            shape = self.canvas.selectedShape  # self.canvas.selectedShape：当前选中的rect
            if shape:
                self.tempDict = shape.label
                self.showStatus(shape.label)
            else:
                self.init_color()
        self.action_edit.setEnabled(selected)
        self.action_delete.setEnabled(selected)
        # self.action_copy.setEnabled(selected)
    
    def newShape(self):
        json_data = copy.deepcopy(FORMAT_DICT_DEFAULT)
        self.canvas.mode_to_edit()
        if json_data is not None:
            self.canvas.setLastLabel(json_data)
            self.tempDict = json_data
            self.showStatus(json_data)
    
    def copyShape(self):
        self.canvas.endMove(copy=True)
        labels = self.canvas.selectedShape.label
        self.canvas.copySelectedShape()
        self.canvas.setLastLabel(labels)
    
    def moveShape(self):
        self.canvas.endMove(copy=False)
        # self.setDirty()
    
    def copySelectedShape(self):
        labels = self.canvas.selectedShape.label
        self.canvas.copySelectedShape()
        self.canvas.setLastLabel(labels)
        
        # fix copy and delete
        # self.shapeSelectionChanged(True)
    
    def save_current_json(self):
        """以json格式保存(ctrl+s)
        """
        def format_shape(s):
            return dict(labels=s.label,
                        position=[{'x': int(p.x()), 'y': int(p.y())} for index, p in enumerate(s.points) if index == 0 or index == 2])
        if self.canvas.shapes:
            shapes = [format_shape(shape) for shape in self.canvas.shapes]
            self.save_as_json(shapes)
        else:
            json_path = self.seleDir + '\\' + self.dir_list[self.dir_show_num].split('.', 2)[0] + '.json'
            if os.path.exists(json_path):
                os.remove(json_path)
        
    def save_as_json(self, data):
        """以json格式保存label"""
        json_path = self.seleDir + '\\' + self.dir_list[self.dir_show_num].split('.', 2)[0] + '.json'
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    
    def fileitemDoubleClicked(self, item=None):
        # 在跳转前需要先保存当前的json
        self.save_current_json()
        
        currIndex = self.dir_list.index((item.text()))
        if currIndex < len(self.dir_list):
            self.dir_show_num = currIndex
            self.show_img_list_change()
            self.show_path_name()
            self.showImg()
    
    def show_filenames_in_list_widget(self, param_img_list):
        """将img展示在listWidget中"""
        for index, imgPath in enumerate(param_img_list):
            item = QtWidgets.QListWidgetItem(imgPath)
            self.listWidget.addItem(item)
    
    def func_message_show(self, param_string):
        """用户提示框"""
        QtWidgets.QMessageBox.warning(
            self, 'WARNING', param_string,
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes
        )
    
    def show_img_list_change(self):
        """增加用户识别，会让读取的dir，有一种印上去的感觉"""
        self.listWidget.item(self.dir_show_num).setSelected(True)
    
    def get_natsorted_file_list(self):
        if self.seleDir is not None:
            file_list = []
            for file in os.listdir(self.seleDir):
                if file.lower().endswith('.png') or file.lower().endswith('.jpg') or file.lower().endswith('.jepg'):
                    file_list.append(file)
            return natsorted(file_list)
    
    def select_root_dir(self):
        """选择文件夹"""
        # re
        self.dir_list = None
        self.dir_show_num = 0
        self.canvas.shapes = []
        
        # func
        self.seleDir = QtWidgets.QFileDialog.getExistingDirectory(self, '请选择打开的目录')
        if self.seleDir == '':
            return
        self.deal_with_dir_list()
        self.init_button_func()
    
    def deal_with_dir_list(self):
        self.dir_list = self.get_natsorted_file_list()
        
        self.listWidget.clear()
        self.show_filenames_in_list_widget(self.dir_list)
        
        self.dir_quantity = len(self.dir_list)
        self.label_all.setText('/' + str(self.dir_quantity))
        self.label_one.setText("当前：" + str(self.dir_show_num + 1))  # 0+1=1
        
        self.show_img_list_change()
        
        # 展示图片和路径
        self.show_path_name()
        self.showImg()
        
        # json
        self.forward_json()
        
        # 让使用者直观的看到变化
        if self.tempDict:
            self.showStatus(self.tempDict)
    
    def show_path_name(self):
        if self.dir_list[self.dir_show_num]:
            self.label_dirName.setText("当前处理的路径为：" + self.seleDir + '/' + self.dir_list[self.dir_show_num])
    
    def json_data_dis(self, json_data, param_label):
        if param_label in json_data.keys():
            self.tempDict[param_label] = json_data[param_label]
    
    def forward_json(self):
        json_path = self.seleDir + '\\' + self.dir_list[self.dir_show_num].split('.', 2)[0] + '.json'
        
        if os.path.exists(json_path):
            with open(json_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                # self.tempDict = data[0]['labels']
                # print(self.tempDict)
                # print(data)
                for shape in data:
                    points = shape['position']
                    label = shape['labels']
                    start_point = QtCore.QPointF(points[0]['x'], points[0]['y'])  # 左上
                    end_point = QtCore.QPointF(points[1]['x'], points[1]['y'])    # 右下
                    
                    two_points = Shape()
                    two_points.addPoint(start_point)
                    two_points.addPoint(end_point)
                    four_points = self.canvas.points_to_point_four(copy.deepcopy(two_points))
                    
                    with_points_shape = Shape()
                    with_points_shape.points = four_points
                    with_points_shape.close()  # 闭合最后一条线
                    self.canvas.shapes.append(with_points_shape)
                    self.canvas.shapes[-1].label = label
                self.canvas.repaint()
        else:
            self.tempDict = copy.deepcopy(self.exampleDict)
    
    def showImg(self):
        # 图片展示
        # print(self.seleDir + '/' + self.dir_list[self.dir_show_num])
        # C:/Users/hwx827939/Desktop/pic/20200310-094603(eSpace).png
        self.canvas_show_sth(self.seleDir + '/' + self.dir_list[self.dir_show_num])
        
        # 图片信息展示
        self.label_one.setText("当前：" + str(self.dir_show_num + 1))
    
    def canvas_show_sth(self, imagepath):
        # imagepath = r'D:\task\300\0300_310.jpg'
        image = QtGui.QImage(imagepath)
        self.canvas.load_pixmap(QtGui.QPixmap.fromImage(image))
        
        # canvas fit window
        self.file_or_dir_fit_window()
    
    def file_or_dir_fit_window(self):
        self.canvas.scale = self.scale_fit_window()  # 随之变动
        self.canvas.repaint()
    
    def scale_fit_window(self):
        e = 2.0  # So that no scrollbars are generated.
        w1 = self.scrollArea.width() - e
        h1 = self.scrollArea.height() - e
        a1 = w1 / h1  # 宽高比a1  例如：16:9
        w2 = self.canvas.pixmap.width() - 0.0
        h2 = self.canvas.pixmap.height() - 0.0
        a2 = w2 / h2
        return w1 / w2 if a2 >= a1 else h1 / h2
    
    def last_dir(self):
        if self.dir_list is not None:
            if self.action_autosave.isChecked():
                self.save_current_json()
            if self.dir_show_num > 0:
                self.canvas.shapes = []
                self.dir_show_num -= 1
                self.show_img_list_change()
                self.show_path_name()
                self.showImg()
                self.forward_json()
    
    def next_dir(self):
        if self.dir_list is not None:
            # 自动保存
            if self.action_autosave.isChecked():
                self.save_current_json()
            
            if self.dir_show_num < self.dir_quantity - 1:
                # re
                self.canvas.shapes = []
                
                # func
                self.dir_show_num += 1
                self.show_img_list_change()
                self.show_path_name()
                self.showImg()
                self.forward_json()
    
    def creating(self):
        return self.mode == self.CREATE
    
    def editing(self):
        return self.mode == self.EDIT
    
    def mode_to_create(self):
        self.canvas.mode_to_create()
    
    def mode_to_edit(self):
        self.canvas.mode_to_edit()
    
    def init_color(self):
        self.button_list[0].setStyleSheet("")
        self.button_list[1].setStyleSheet("")
        self.button_list[2].setStyleSheet("")
        self.button_list[3].setStyleSheet("")
        self.button_list[4].setStyleSheet("")
        self.button_list[5].setStyleSheet("")
        self.button_list[6].setStyleSheet("")
        self.button_list[7].setStyleSheet("")
        self.button_list[8].setStyleSheet("")
        self.button_list[9].setStyleSheet("")
        self.button_list[10].setStyleSheet("")
        self.button_list[11].setStyleSheet("")
        self.button_list[12].setStyleSheet("")
        self.button_list[13].setStyleSheet("")
        self.button_list[14].setStyleSheet("")
        self.button_list[15].setStyleSheet("")
        self.button_list[16].setStyleSheet("")
        self.button_list[17].setStyleSheet("")
    
    def color(self, label_dict, param_attribute, param_state, param_button):
        if label_dict[param_attribute] == param_state:
            param_button.setStyleSheet("background-color: rgb(49, 247, 244);")
        else:
            param_button.setStyleSheet("")
    
    def showStatus(self, label_dict):
        self.color(label_dict, FORMAT_DICT_KEY_LIST[0], FORMAT_DICT_DICT_LIST['backlight'][0], self.button_list[0])
        self.color(label_dict, FORMAT_DICT_KEY_LIST[0], FORMAT_DICT_DICT_LIST['backlight'][1], self.button_list[1])
        
        self.color(label_dict, FORMAT_DICT_KEY_LIST[1], FORMAT_DICT_DICT_LIST['hasGlove'][0], self.button_list[2])
        self.color(label_dict, FORMAT_DICT_KEY_LIST[1], FORMAT_DICT_DICT_LIST['hasGlove'][1], self.button_list[3])
        
        self.color(label_dict, FORMAT_DICT_KEY_LIST[2], FORMAT_DICT_DICT_LIST['resolution'][0], self.button_list[4])
        self.color(label_dict, FORMAT_DICT_KEY_LIST[2], FORMAT_DICT_DICT_LIST['resolution'][1], self.button_list[5])
        self.color(label_dict, FORMAT_DICT_KEY_LIST[2], FORMAT_DICT_DICT_LIST['resolution'][2], self.button_list[6])
        self.color(label_dict, FORMAT_DICT_KEY_LIST[2], FORMAT_DICT_DICT_LIST['resolution'][3], self.button_list[7])
        
        self.color(label_dict, FORMAT_DICT_KEY_LIST[3], FORMAT_DICT_DICT_LIST['immerse'][0], self.button_list[8])
        self.color(label_dict, FORMAT_DICT_KEY_LIST[3], FORMAT_DICT_DICT_LIST['immerse'][1], self.button_list[9])
        
        self.color(label_dict, FORMAT_DICT_KEY_LIST[4], FORMAT_DICT_DICT_LIST['lightOn'][0], self.button_list[10])
        self.color(label_dict, FORMAT_DICT_KEY_LIST[4], FORMAT_DICT_DICT_LIST['lightOn'][1], self.button_list[11])
        
        self.color(label_dict, FORMAT_DICT_KEY_LIST[5], FORMAT_DICT_DICT_LIST['integrity'][0], self.button_list[12])
        self.color(label_dict, FORMAT_DICT_KEY_LIST[5], FORMAT_DICT_DICT_LIST['integrity'][1], self.button_list[13])
        self.color(label_dict, FORMAT_DICT_KEY_LIST[5], FORMAT_DICT_DICT_LIST['integrity'][2], self.button_list[14])
        self.color(label_dict, FORMAT_DICT_KEY_LIST[5], FORMAT_DICT_DICT_LIST['integrity'][3], self.button_list[15])
        
        self.color(label_dict, FORMAT_DICT_KEY_LIST[6], FORMAT_DICT_DICT_LIST['angle'][0], self.button_list[16])
        self.color(label_dict, FORMAT_DICT_KEY_LIST[6], FORMAT_DICT_DICT_LIST['angle'][1], self.button_list[17])
    
    def input_json_data(self, param_attribute, param_state):
        self.tempDict[param_attribute] = param_state
        self.showStatus(self.tempDict)
    
    def backlight_yes(self):
        self.input_json_data(FORMAT_DICT_KEY_LIST[0], FORMAT_DICT_DICT_LIST['backlight'][0])
    
    def backlight_no(self):
        self.input_json_data(FORMAT_DICT_KEY_LIST[0], FORMAT_DICT_DICT_LIST['backlight'][1])
    
    def hasGlove_yes(self):
        self.input_json_data(FORMAT_DICT_KEY_LIST[1], FORMAT_DICT_DICT_LIST['hasGlove'][0])
    
    def hasGlove_no(self):
        self.input_json_data(FORMAT_DICT_KEY_LIST[1], FORMAT_DICT_DICT_LIST['hasGlove'][1])
    
    def resolution_clear(self):
        self.input_json_data(FORMAT_DICT_KEY_LIST[2], FORMAT_DICT_DICT_LIST['resolution'][0])
    
    def resolution_blur(self):
        self.input_json_data(FORMAT_DICT_KEY_LIST[2], FORMAT_DICT_DICT_LIST['resolution'][1])
    
    def resolution_dark(self):
        self.input_json_data(FORMAT_DICT_KEY_LIST[2], FORMAT_DICT_DICT_LIST['resolution'][2])
    
    def resolution_invisible(self):
        self.input_json_data(FORMAT_DICT_KEY_LIST[2], FORMAT_DICT_DICT_LIST['resolution'][3])
    
    def immerse_yes(self):
        self.input_json_data(FORMAT_DICT_KEY_LIST[3], FORMAT_DICT_DICT_LIST['immerse'][0])
        
    def immerse_no(self):
        self.input_json_data(FORMAT_DICT_KEY_LIST[3], FORMAT_DICT_DICT_LIST['immerse'][1])
        
    def lightOn_on(self):
        self.input_json_data(FORMAT_DICT_KEY_LIST[4], FORMAT_DICT_DICT_LIST['lightOn'][0])
        
    def lightOn_off(self):
        self.input_json_data(FORMAT_DICT_KEY_LIST[4], FORMAT_DICT_DICT_LIST['lightOn'][1])
    
    def integrity_full(self):
        self.input_json_data(FORMAT_DICT_KEY_LIST[5], FORMAT_DICT_DICT_LIST['integrity'][0])
    
    def integrity_complete(self):
        self.input_json_data(FORMAT_DICT_KEY_LIST[5], FORMAT_DICT_DICT_LIST['integrity'][1])
    
    def integrity_incomplete(self):
        self.input_json_data(FORMAT_DICT_KEY_LIST[5], FORMAT_DICT_DICT_LIST['integrity'][2])
        
    def integrity_nodevice(self):
        self.input_json_data(FORMAT_DICT_KEY_LIST[5], FORMAT_DICT_DICT_LIST['integrity'][3])
    
    def angle_front(self):
        self.input_json_data(FORMAT_DICT_KEY_LIST[6], FORMAT_DICT_DICT_LIST['angle'][0])
        
    def angle_side(self):
        self.input_json_data(FORMAT_DICT_KEY_LIST[6], FORMAT_DICT_DICT_LIST['angle'][1])


def get_main_app():
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.showMaximized()
    return app, win


def main():
    app, win = get_main_app()
    return app.exec_()


if __name__ == "__main__":
    sys.exit(main())
