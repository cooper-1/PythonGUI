# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled2.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_Test(object):
    def setupUi(self, Test):
        Test.setObjectName("Test")
        Test.resize(551, 384)
        self.centralwidget = QtWidgets.QWidget(Test)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 230, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 80, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 150, 72, 15))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 230, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 80, 271, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 140, 271, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        Test.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Test)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 551, 26))
        self.menubar.setObjectName("menubar")
        Test.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Test)
        self.statusbar.setObjectName("statusbar")
        Test.setStatusBar(self.statusbar)

        # ??????????????????
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('k1.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Test.setWindowIcon(icon)
        # ??????????????????
        # Test.setStyleSheet('#Test{background-color:gray}')
        # ??????????????????
        # Test.setStyleSheet('#Test{border-image:url(Kasumigaoka1.jpg)}')
        # ???????????????????????????
        # palette=QtGui.QPalette()
        # palette.setColor(QtGui.QPalette.Background,Qt.red)
        # Test.setPalette(palette)
        # ??????Qpalette????????????????????????

        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Background, QBrush(QPixmap('k1.png')))
        # ??????Qpalette????????????????????????(????????????????????????)
        palette.setBrush(Test.backgroundRole(), QBrush(QPixmap('k1.png').scaled(Test.size(),
        QtCore.Qt.IgnoreAspectRatio,QtCore.Qt.SmoothTransformation)))
        Test.setPalette(palette)

        self.retranslateUi(Test)
        QtCore.QMetaObject.connectSlotsByName(Test)

    def retranslateUi(self, Test):
        _translate = QtCore.QCoreApplication.translate
        Test.setWindowTitle('?????????')
        self.pushButton_3.setText(_translate("Test", "??????"))
        self.label.setText(_translate("Test", "?????????"))
        self.label_2.setText(_translate("Test", "?????????"))
        self.pushButton.setText(_translate("Test", "??????"))


import sys  # ??????????????????


def show_MainWindow():
    app = QtWidgets.QApplication(sys.argv)  # ?????????QApplication????????????GUI???????????????
    MainWindow = QtWidgets.QMainWindow()  # ??????MainWindow
    ui = Ui_Test()  # ?????????ui???
    ui.setupUi(MainWindow)  # ????????????UI
    MainWindow.show()  # ????????????
    sys.exit(app.exec_())  # ??????????????????????????????????????????????????????


if __name__ == "__main__":
    show_MainWindow()
