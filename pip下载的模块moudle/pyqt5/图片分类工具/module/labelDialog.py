from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

BB = QDialogButtonBox
__moudlename__ = "输入一个类名"


class LabelDialog(QDialog):
    
    def __init__(self, text="在此输入标签", parent=None, listItem=None):
        super(LabelDialog, self).__init__(parent)
        
        self.setWindowTitle(__moudlename__)  # 标题
        
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
        layout.addWidget(self.edit)
        self.buttonBox = bb = BB(BB.Ok | BB.Cancel, Qt.Horizontal, self)
        bb.button(BB.Ok).setIcon(QIcon(":/icons/" + 'done.png'))
        bb.button(BB.Cancel).setIcon(QIcon(":/icons/" + 'undo.png'))
        bb.accepted.connect(self.validate)  # ok
        bb.rejected.connect(self.reject)    # cancel
        layout.addWidget(bb)
        
        # # 展示出label标签，可供选择
        # if listItem is not None and len(listItem) > 0:
        #     self.listWidget = QListWidget(self)
        #     for item in listItem:
        #         self.listWidget.addItem(item)
        #     self.listWidget.itemClicked.connect(self.listItemClick)
        #     self.listWidget.itemDoubleClicked.connect(self.listItemDoubleClick)
        #     layout.addWidget(self.listWidget)

        self.setLayout(layout)
    
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
