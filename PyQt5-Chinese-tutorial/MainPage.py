# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainPage.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        MainWindow.insertToolBarBreak(self.toolBar)
        self.actionclose = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionclose.setIcon(icon)
        self.actionclose.setObjectName("actionclose")
        self.actionImportFile = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/icons8-add-folder-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionImportFile.setIcon(icon1)
        self.actionImportFile.setObjectName("actionImportFile")
        self.menubar.addAction(self.menu_File.menuAction())
        self.toolBar.addAction(self.actionImportFile)
        self.toolBar.addAction(self.actionclose)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionclose.setText(_translate("MainWindow", "close"))
        self.actionclose.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionImportFile.setText(_translate("MainWindow", "ImportFile"))


