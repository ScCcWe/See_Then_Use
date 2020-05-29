# !/usr/bin/python 
# -*- coding: utf-8 -*-
# file_name: labelDialog_canvas.py
# function：None
# need_module: None
# author: ScCcWe
# time: 2020/2/25 13:51


from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from PyQt5 import QtGui
from canvas import Canvas
from PyQt5 import QtCore, QtWidgets

BB = QDialogButtonBox
__moudlename__ = "查看图片细节"


class LabelDialog(QDialog):
    MODE_FIT_WINDOW, MODE_ADJUST_SIZE = ['F', 'A']
    
    LIST_SIZE = [0, 0, 2200, 1200]
    
    def __init__(self, text="在此输入标签", parent=None, listItem=None, pic_path=None):
        super(LabelDialog, self).__init__(parent)
        self.setWindowTitle(__moudlename__)  # 标题
        
        self.setGeometry(self.LIST_SIZE[0], self.LIST_SIZE[1], self.LIST_SIZE[2], self.LIST_SIZE[3])
        
        self.edit = QLineEdit()
        self.edit.setText(text)
        self.edit.setValidator(self.labelValidator())
        self.edit.editingFinished.connect(self.postProcess)
        
        model = QStringListModel()
        # model.setStringList(listItem)
        completer = QCompleter()
        completer.setModel(model)
        self.edit.setCompleter(completer)
        
        layout = QVBoxLayout()
        
        self.pic_path = pic_path
        
        # 展示图片
        try:
            self.mode = self.MODE_FIT_WINDOW
            
            self.canvas = Canvas(parent=self)
            self.scrollArea = QScrollArea()
            self.scrollArea.setGeometry(QtCore.QRect(self.LIST_SIZE[0], self.LIST_SIZE[1], self.LIST_SIZE[2], self.LIST_SIZE[3]))
            image = QImage(self.pic_path)
            self.canvas.load_pixmap(QPixmap.fromImage(image))
            # print('self.scale_fit_window():', self.scale_fit_window())
            self.file_or_dir_fit_window()
            
            self.scrollArea.setWidget(self.canvas)
            self.scrollArea.setWidgetResizable(True)
            layout.addWidget(self.scrollArea)
            self.setLayout(layout)
        except Exception as e:
            print('Error:', e)
    
    def scale_fit_window(self):
        e = 2.0  # So that no scrollbars are generated.
        w1 = self.scrollArea.width() - e
        h1 = self.scrollArea.height() - e
        a1 = w1 / h1  # 宽高比a1  例如：16:9
        w2 = self.canvas.pixmap.width() - 0.0
        h2 = self.canvas.pixmap.height() - 0.0
        a2 = w2 / h2
        return w1 / w2 if a2 >= a1 else h1 / h2
    
    def file_or_dir_fit_window(self):
        if self.mode == self.MODE_FIT_WINDOW:
            self.canvas.scale = self.scale_fit_window()  # 随之变动
            self.canvas.adjustSize()
            self.repaint()
        elif self.mode == self.MODE_ADJUST_SIZE:
            self.canvas.adjustSize()
            self.update()
    
    @staticmethod
    def labelValidator():
        return QRegExpValidator(QRegExp(r'^[^ \t].+'), None)
    
    def validate(self):
        if self.edit.text().strip():
            self.accept()
    
    def postProcess(self):
        self.edit.setText(self.edit.text())
    
    def popUp(self, text='', move=True):
        self.edit.setText(text)
        self.edit.setSelection(0, len(text))
        self.edit.setFocus(Qt.PopupFocusReason)
        # if move:
        #     self.move(QCursor.pos())
        return self.edit.text() if self.exec_() else None
    
    def listItemClick(self, tQListWidgetItem):
        text = tQListWidgetItem.text().strip()
        self.edit.setText(text)
    
    def listItemDoubleClick(self, tQListWidgetItem):
        self.listItemClick(tQListWidgetItem)
        self.validate()


if __name__ == "__main__":
    # 需要删除parent才能运行
    app = QApplication(sys.argv)
    win = LabelDialog()
    win.show()
    sys.exit(app.exec_())
