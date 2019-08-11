# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'projeto.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(416, 164)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.somabt = QtWidgets.QPushButton(self.centralwidget)
        self.somabt.setGeometry(QtCore.QRect(90, 80, 81, 41))
        self.somabt.setObjectName("somabt")
        self.somabt.clicked.connect(self.a)
        self.result = QtWidgets.QLCDNumber(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(300, 20, 81, 51))
        self.result.setObjectName("result")
        self.text1 = QtWidgets.QTextEdit(self.centralwidget)
        self.text1.setGeometry(QtCore.QRect(10, 30, 104, 31))
        self.text1.setObjectName("text1")
        self.text1.setInput()
        self.text2 = QtWidgets.QTextEdit(self.centralwidget)
        self.text2.setGeometry(QtCore.QRect(150, 30, 104, 31))
        self.text2.setObjectName("text2")
        self.text2.setInput()
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 20, 31, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 20, 31, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 416, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    
    def a(self):
        x = str(self.text1.input())
        y = str(self.text2.input())
        z = x+y
        print(z)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.somabt.setText(_translate("MainWindow", "Soma"))
        self.label.setText(_translate("MainWindow", "+"))
        self.label_2.setText(_translate("MainWindow", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
