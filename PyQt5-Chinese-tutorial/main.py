
import sys

from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog,qApp,QMessageBox,\
                             QWidget,QVBoxLayout,QPlainTextEdit, QHBoxLayout,QTabWidget
from PyQt5.QtGui import QColor, QPainter

from MainPage import Ui_MainWindow

lineBarColor = QColor(53, 53, 53)
lineHighlightColor = QColor('#00FF04')

class NumberBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.editor = parent
        layout = QVBoxLayout(self)
        self.editor.blockCountChanged.connect(self.update_width)
        self.editor.updateRequest.connect(self.update_on_scroll)
        self.update_width('1')

    def mousePressEvent(self, QMouseEvent):
        print("class NumberBar(QWidget):mousePressEvent")

    def update_on_scroll(self, rect, scroll):
        if self.isVisible():
            if scroll:
                self.scroll(0, scroll)
            else:
                self.update()

    def update_width(self, string):
        width = self.fontMetrics().width(str(string)) + 10
        print("update_width:width:" + str(width))
        if self.width() != width:
            self.setFixedWidth(width)

    def paintEvent(self, event):
        if self.isVisible():
            block = self.editor.firstVisibleBlock()
            height = self.fontMetrics().height()
            number = block.blockNumber()
            painter = QPainter(self)
            painter.fillRect(event.rect(), lineBarColor)
            painter.drawRect(0, 0, event.rect().width() - 1, event.rect().height() - 1)
            font = painter.font()

            current_block = self.editor.textCursor().block().blockNumber() + 1

            while block.isValid():
                block_geometry = self.editor.blockBoundingGeometry(block)
                offset = self.editor.contentOffset()
                block_top = block_geometry.translated(offset).top()
                number += 1

                rect = QRect(0, block_top, self.width() - 5, height)

                if number == current_block:
                    font.setBold(True)
                else:
                    font.setBold(False)

                painter.setFont(font)
                painter.drawText(rect, Qt.AlignRight, '%i' % number)

                if block_top > event.rect().bottom():
                    break

                block = block.next()

            painter.end()

class Content(QWidget):
    def __init__(self, text):
        super(Content, self).__init__()
        self.editor = QPlainTextEdit()
        self.editor.setPlainText(text)
        # Create a layout for the line numbers

        self.hbox = QHBoxLayout(self)
        self.numbers = NumberBar(self.editor)
        self.hbox.addWidget(self.numbers)
        self.hbox.addWidget(self.editor)

class Content_Excel(QWidget):
    def __init__(self, text):
        super(Content, self).__init__()
        self.editor = QPlainTextEdit()
        self.editor.setPlainText(text)
        # Create a layout for the line numbers

        self.hbox = QHBoxLayout(self)
        self.numbers = NumberBar(self.editor)
        self.hbox.addWidget(self.numbers)
        self.hbox.addWidget(self.editor)


class MyTableWidget(QWidget):

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tabs.resize(300, 200)

        # Add tabs
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.closeTab)
        self.tabs.currentChanged['int'].connect(self.tabfun)


        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        #self.tabs.toolTip(self.tabs.tipsText)
        self.setLayout(self.layout)

    def closeTab(self, index):
        tab = self.tabs.widget(index)
        tab.deleteLater()
        self.tabs.removeTab(index)

    def addtab(self, content, fileName):

        self.tabs.addTab(Content(str(content)), str(fileName))



    def tabfun(selfself,index): # test the current index number
        print("The current page is : " +str(index))




class MyMainWindow (QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MyMainWindow,self).__init__(parent)

        self.setupUi(self)
        self.action_Exit.triggered.connect(qApp.quit)
        #self.actionOpen_File.triggered.connect(self.openfile_New)
        self.actionImportFile.triggered.connect(self.openFile)


        self.tabs = MyTableWidget()
        self.setCentralWidget(self.tabs)

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

    def openfile_refer(self):  #for reference
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

    def openFile(self):
        options = QFileDialog.Options()
        filenames, _ = QFileDialog.getOpenFileNames(
            self, 'Open a file', '',
            'All Files (*);;Python Files (*.py);;Text Files (*.txt)',
            options=options
        )
        if filenames:
            for filename in filenames:
                with open(filename, 'r+') as file_o:
                    text = file_o.read()
                    self.tabs.addtab(text, filename)

    def test(self):
        reply = QMessageBox.information(self,
                                        "Title",
                                        "Information",
                                        QMessageBox.Yes | QMessageBox.No)




if __name__=="__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())