# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '使用资源文件设置背景2.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Test(object):
    def setupUi(self, Test):
        Test.setObjectName("Test")
        Test.resize(551, 384)
        Test.setWindowOpacity(0.5)
        self.centralwidget = QtWidgets.QWidget(Test)
        self.centralwidget.setStyleSheet("border-image: url(:/png/Kasumigaoka1.jpg);")
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

        self.retranslateUi(Test)
        # 关闭主窗口
        self.pushButton.clicked.connect(Test.close)
        QtCore.QMetaObject.connectSlotsByName(Test)

    def retranslateUi(self, Test):
        _translate = QtCore.QCoreApplication.translate
        Test.setWindowTitle(_translate("Test", "MainWindow"))
        self.pushButton_3.setText(_translate("Test", "登录"))
        self.label.setText(_translate("Test", "账号："))
        self.label_2.setText(_translate("Test", "密码："))
        self.pushButton.setText(_translate("Test", "退出"))
import img_rc

import sys  # 导入系统模块


def show_MainWindow():
    app = QtWidgets.QApplication(sys.argv)  # 实例化QApplication类，作为GUI主程序入口
    MainWindow = QtWidgets.QMainWindow()    # 创建MainWindow
    ui = Ui_Test()                          # 实例化ui类
    ui.setupUi(MainWindow)                  # 设置窗口UI
    MainWindow.show()                       # 显示窗口
    sys.exit(app.exec_())                   # 当窗口创建完成时，需要结束主循环过程


if __name__ == "__main__":
    show_MainWindow()