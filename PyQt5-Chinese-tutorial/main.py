
import sys
from PyQt5.QtWidgets import (QApplication,QMainWindow,QFileDialog,qApp,QMessageBox)
from PyQt5 import QtGui
from MainPage import *


class MyMainWindow (QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MyMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.action_Exit.triggered.connect(qApp.quit)
        self.actionOpen_File.triggered.connect(self.openfile_New)
        self.actionImportFile.triggered.connect(self.test)
        self.isChanged = 0

    def file_open(self):
        name = QFileDialog.getOpenFileName(self, 'Open File')
        file = open(name, 'r')

        self.editor()
        with file:
            text = file.read()
            self.textEdit.setText(text)

    def editor(self):
        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)

    def openfile_New(self):
        if self.isChanged == True:
            quit_msg = "<b>The Document was changed.<br>Do you want to save changes?</ b>"
            reply = QMessageBox.question(self, 'Save Confirmation',quit_msg, QMessageBox.Yes, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.saveOnQuit()
        fileName,_ = QFileDialog.getOpenFileName(self, "Select file", "./",
                                                   "Bom file(*.txt *.csv *.xlsx *.xlsm *.xls);; \
                                                   Text Files (*.txt);; \
                                    Excel file (*.csv *.xlsx *.xlsm *.xls)")
        if fileName:
            #self.loadCsvOnOpen(fileName)
            QMessageBox.warning(self,'','Get!'+ fileName)

    def test(self):
        reply = QMessageBox.information(self,  # 使用infomation信息框
                                        "标题",
                                        "消息",
                                        QMessageBox.Yes | QMessageBox.No)




if __name__=="__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())