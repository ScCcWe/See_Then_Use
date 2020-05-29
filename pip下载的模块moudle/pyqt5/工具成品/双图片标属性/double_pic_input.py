# encoding: utf-8
# !/user/bin/env python
"""
双图阴影标注
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
from PyQt5.QtCore import Qt
from UI import Ui_MainWindow
from labelDialog_canvas import LabelDialog


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    
    LABEL_IMG_LIST = ['light.jpg', 'shadow.jpg']
    # LABEL_IMG_LIST = ['lightout.jpg', 'shadowout.jpg']
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.dir_list = []
        self.dir_quantity = 0
        self.seleDir = None
        self.dir_show_num = 0
        
        # self.exampleDict = {'problems': '',
        #                     'shadow': '',
        #                     'lightSource': '',
        #                     'hardSample': '',
        #                     'qualified': ''}
        self.exampleDict = {'是否合格': '',
                            '阴影是否清晰': '',
                            '阴影深浅': '',
                            '阴影大小': ''}
        self.tempDict = None
        # self.lineEdit.setText("可在此处输入跳转值...")
        
        # 图片细节展示模块
        self.labelHist = None  # 暂时没用到
        
        # img_list
        self.label_img_list = self.LABEL_IMG_LIST
    
    def show_detail(self):
        try:
            self.pic_path = self.seleDir + '\\' + self.dir_list[self.dir_show_num] + '\\' + self.label_img_list[0]
            self.label_dialog = LabelDialog(parent=self, listItem=self.labelHist, pic_path=self.pic_path)
            self.label_dialog.popUp(text='')
        except Exception as e:
            print('Error:', e)
    
    def show_detail_right(self):
        self.pic_path = self.seleDir + '\\' + self.dir_list[self.dir_show_num] + '\\' + self.label_img_list[1]
        self.label_dialog = LabelDialog(parent=self, listItem=self.labelHist, pic_path=self.pic_path)
        self.label_dialog.popUp(text='')
    
    def select_root_dir(self):
        try:
            self.dir_list = []
            self.dir_show_num = 0
            
            self.seleDir = QtWidgets.QFileDialog.getExistingDirectory(self, '选择打开的目录')
            
            if self.seleDir == '':
                return
            
            self.dir_list = natsorted(os.listdir(self.seleDir))
            
            self.dir_quantity = len(self.dir_list)
            self.label_all.setText('/' + str(self.dir_quantity))
            self.label_one.setText(str(self.dir_show_num + 1))  # 0+1=1
            
            self.tempDict = copy.deepcopy(self.exampleDict)
            
            self.show_path_name()
            self.showImg()
        except Exception as e:
            print("Error in select_root_dir:", e)
    
    def show_path_name(self):
        if self.dir_list[self.dir_show_num]:
            self.label_dirName.setText("当前处理的路径为：" + self.seleDir + '/' + self.dir_list[self.dir_show_num])
    
    def showImg(self):
        json_path = self.seleDir + '\\' + self.dir_list[self.dir_show_num] + \
                    '\\' + self.dir_list[self.dir_show_num] + '.json'
        if os.path.exists(json_path):
            with open(json_path, "r", encoding="utf-8") as f:
                self.tempDict = json.load(f)
                # self.tempDict = json.loads(f.read())
        
        else:
            self.tempDict = copy.deepcopy(self.exampleDict)
            # self.tempDict['imageName'] = self.dir_list[self.dir_show_num]
        # img_list = os.listdir(os.path.join(self.seleDir, self.dir_list[self.dir_show_num]))
        # # for x in img_list:
        # #     if x.endswith('.json'):
        # #         img_list.remove(x)
        # print(img_list[0])
        # print(img_list[1])
        # print(img_list[2])
        self.label_img1.setPixmap(
            QtGui.QPixmap(self.seleDir + '\\' + self.dir_list[self.dir_show_num] + '\\' + self.label_img_list[0]).scaled(800, 800, Qt.KeepAspectRatio))
        self.label_img2.setPixmap(
            QtGui.QPixmap(self.seleDir + '\\' + self.dir_list[self.dir_show_num] + '\\' + self.label_img_list[1]).scaled(800, 800, Qt.KeepAspectRatio))
        self.label_one.setText(str(self.dir_show_num + 1))
        self.showStatus()
    
    def last_dir(self):
        self.white_color()
        json_path = self.seleDir + '\\' + self.dir_list[self.dir_show_num] + '\\' + self.dir_list[
            self.dir_show_num] + '.json'
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(self.tempDict, f, indent=4, ensure_ascii=False)
        
        if self.dir_show_num > 0:
            self.dir_show_num -= 1
            self.show_path_name()
            self.showImg()
        else:
            QtWidgets.QMessageBox.warning(
                self, 'WARNING', '已经没有上一张啦！！！',
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)
    
    def next_dir(self):
        self.white_color()
        json_path = self.seleDir + '\\' + self.dir_list[self.dir_show_num] + '\\' + self.dir_list[
            self.dir_show_num] + '.json'
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(self.tempDict, f, indent=4, ensure_ascii=False)
        
        if self.dir_show_num < self.dir_quantity - 1:
            self.dir_show_num += 1
            self.show_path_name()
            self.showImg()
        else:
            QtWidgets.QMessageBox.warning(
                self, 'WARNING', '不能再往前拉！！！',
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)
    
    def jump_to_dir(self):
        """跳转"""
        try:
            self.dir_show_num = int(self.lineEdit.text()) - 1  # 输入7，实际去6
            if self.dir_quantity > self.dir_show_num > -1:
                self.show_path_name()
                self.showImg()
            else:
                QtWidgets.QMessageBox.warning(
                    self, 'WARNING', '您的输入有误，无法实现跳转！请重新输入！！！',
                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)
        except Exception as e:
            print('eRROR IN JUMP', e)
    
    """可以改写！！！"""
    
    def button_show_color(self, param_attribute, param_state, param_button):
        if self.tempDict[param_attribute] == param_state:
            param_button.setStyleSheet("background-color: rgb(49, 247, 244);")
        else:
            param_button.setStyleSheet("")
    
    def showStatus(self):
        # 首先判断是否合格
        self.button_show_color('是否合格', '合格', self.pushButton_pro1)
        self.button_show_color('是否合格', '不合格', self.pushButton_pro2)
        
        # 只有合格，三个属性才能标注
        if self.tempDict['是否合格'] == '合格':
            self.button_show_color('阴影是否清晰', '清晰', self.pushButton_sha1)
            self.button_show_color('阴影是否清晰', '不清晰', self.pushButton_sha2)
            self.button_show_color('阴影深浅', '深阴影', self.pushButton_lig1)
            self.button_show_color('阴影深浅', '中等阴影', self.pushButton_lig2_2)
            self.button_show_color('阴影深浅', '浅阴影', self.pushButton_lig2)
            self.button_show_color('阴影大小', '大', self.pushButton_hard1)
            self.button_show_color('阴影大小', '中', self.pushButton_hard2)
            self.button_show_color('阴影大小', '小', self.pushButton_hard2_2)
    
    def white_color(self):
        self.pushButton_pro1.setStyleSheet("")
        self.pushButton_pro2.setStyleSheet("")
        self.pushButton_sha1.setStyleSheet("")
        self.pushButton_sha2.setStyleSheet("")
        self.pushButton_lig1.setStyleSheet("")
        self.pushButton_lig2_2.setStyleSheet("")
        self.pushButton_lig2.setStyleSheet("")
        self.pushButton_hard1.setStyleSheet("")
        self.pushButton_hard2.setStyleSheet("")
        self.pushButton_hard2_2.setStyleSheet("")
    
    # def showStatus(self):
    #     # 是否合格
    #     if self.tempDict['是否合格'] == '合格':
    #         self.pushButton_pro1.setStyleSheet("background-color: rgb(49, 247, 244);")
    #     else:
    #         self.pushButton_pro1.setStyleSheet("")
    #     if self.tempDict['是否合格'] == '不合格':
    #         self.pushButton_pro2.setStyleSheet("background-color: rgb(49, 247, 244);")
    #     else:
    #         self.pushButton_pro2.setStyleSheet("")
    #
    #     # 只有合格才有用
    #     if self.tempDict['阴影是否清晰'] == '清晰' and self.tempDict['是否合格'] != '不合格':
    #         self.pushButton_sha1.setStyleSheet("background-color: rgb(49, 247, 244);")
    #     else:
    #         self.pushButton_sha1.setStyleSheet("")
    #     if self.tempDict['阴影是否清晰'] == '不清晰' and self.tempDict['是否合格'] != '不合格':
    #         self.pushButton_sha2.setStyleSheet("background-color: rgb(49, 247, 244);")
    #     else:
    #         self.pushButton_sha2.setStyleSheet("")
    #
    #     if self.tempDict['阴影深浅'] == '深阴影' and self.tempDict['是否合格'] != '不合格':
    #         self.pushButton_lig1.setStyleSheet("background-color: rgb(49, 247, 244);")
    #     else:
    #         self.pushButton_lig1.setStyleSheet("")
    #     if self.tempDict['阴影深浅'] == '中等阴影' and self.tempDict['是否合格'] != '不合格':
    #         self.pushButton_lig2_2.setStyleSheet("background-color: rgb(49, 247, 244);")
    #     else:
    #         self.pushButton_lig2_2.setStyleSheet("")
    #     if self.tempDict['阴影深浅'] == '浅阴影' and self.tempDict['是否合格'] != '不合格':
    #         self.pushButton_lig2.setStyleSheet("background-color: rgb(49, 247, 244);")
    #     else:
    #         self.pushButton_lig2.setStyleSheet("")
    #
    #     if self.tempDict['阴影大小'] == '大' and self.tempDict['是否合格'] != '不合格':
    #         self.pushButton_hard1.setStyleSheet("background-color: rgb(49, 247, 244);")
    #     else:
    #         self.pushButton_hard1.setStyleSheet("")
    #     if self.tempDict['阴影大小'] == '中' and self.tempDict['是否合格'] != '不合格':
    #         self.pushButton_hard2.setStyleSheet("background-color: rgb(49, 247, 244);")
    #     else:
    #         self.pushButton_hard2.setStyleSheet("")
    #     if self.tempDict['阴影大小'] == '小' and self.tempDict['是否合格'] != '不合格':
    #         self.pushButton_hard2_2.setStyleSheet("background-color: rgb(49, 247, 244);")
    #     else:
    #         self.pushButton_hard2_2.setStyleSheet("")
    
    def hege(self):
        """标注为合格
        两种情况：
            1）空标记为合格
            2）不合格标记为合格
        """
        # 不合格标记为合格
        if self.tempDict['是否合格'] == '不合格':
            self.tempDict = copy.deepcopy(self.exampleDict)
        
        # 空标记为合格
        self.tempDict['是否合格'] = '合格'
        self.showStatus()
    
    def buhege(self):
        
        # 不合格比较特殊，当出现不合格的时候，属性都需要消除
        self.tempDict = copy.deepcopy(self.exampleDict)
        
        self.tempDict['是否合格'] = '不合格'
        
        self.button_show_color('是否合格', '不合格', self.pushButton_pro2)
        print('1')
        self.pushButton_pro1.setStyleSheet("")
        # self.pushButton_pro2.setStyleSheet("")
        self.pushButton_sha1.setStyleSheet("")
        self.pushButton_sha2.setStyleSheet("")
        self.pushButton_lig1.setStyleSheet("")
        self.pushButton_lig2_2.setStyleSheet("")
        self.pushButton_lig2.setStyleSheet("")
        self.pushButton_hard1.setStyleSheet("")
        self.pushButton_hard2.setStyleSheet("")
        self.pushButton_hard2_2.setStyleSheet("")
    
    def input_json_data(self, param_attribute, param_state):
    
        # 只有合格的时候，才需要接下去的三个属性
        if self.tempDict['是否合格'] == '合格':
            self.tempDict[param_attribute] = param_state
        
        self.showStatus()
    
    """阴影是否清晰"""
    
    def qingxi(self):
        self.input_json_data('阴影是否清晰', '清晰')
    
    def buqingxi(self):
        self.input_json_data('阴影是否清晰', '不清晰')
    
    """阴影深浅"""
    
    def shenyinying(self):
        self.input_json_data('阴影深浅', '深阴影')
    
    def zhongdengyinying(self):
        self.input_json_data('阴影深浅', '中等阴影')
    
    def qianyinying(self):
        self.input_json_data('阴影深浅', '浅阴影')

    """阴影大小"""
    
    def da(self):
        self.input_json_data('阴影大小', '大')
    
    def zhong(self):
        self.input_json_data('阴影大小', '中')
    
    def xiao(self):
        self.input_json_data('阴影大小', '小')
    
    def changeShadow(self):
        # self.tempDict初始为None, 如果不是一开始就调用changeShadow(), 则会保存当前的属性
        if self.tempDict:
            json_path = self.seleDir + '\\' + self.dir_list[self.dir_show_num] + '\\' + self.dir_list[
                self.dir_show_num] + '.json'
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(self.tempDict, f, indent=4, ensure_ascii=False)
        
        if self.dir_list != []:
            os.rename(self.seleDir + '\\' + self.dir_list[self.dir_show_num] + '\\' + self.label_img_list[0],
                      self.seleDir + '\\' + self.dir_list[self.dir_show_num] + '\\' + 'tempout.jpg')
            os.rename(self.seleDir + '\\' + self.dir_list[self.dir_show_num] + '\\' + self.label_img_list[1],
                      self.seleDir + '\\' + self.dir_list[self.dir_show_num] + '\\' + self.label_img_list[0])
            os.rename(self.seleDir + '\\' + self.dir_list[self.dir_show_num] + '\\' + 'tempout.jpg',
                      self.seleDir + '\\' + self.dir_list[self.dir_show_num] + '\\' + self.label_img_list[1])
            self.showImg()
        else:
            # 这里可以增加一个提示窗口
            QtWidgets.QMessageBox.warning(
                self, 'WARNING', '请先选择文件夹！！！',
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes
            )
    
    def keyPressEvent(self, event):
        if event.key() == 65:  # A
            self.last_dir()
        if event.key() == 68:  # D
            self.next_dir()
        if event.key() == 87:  # W
            self.changeShadow()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
