# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'withdraw.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as sql
mycon= sql.connect(host="localhost",user="root",password="jehan26122003",database="bank")
mycur= mycon.cursor()



class withdraw(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(467, 178)
        MainWindow.setStyleSheet("background-color: rgb(18, 18, 18);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(10, 20, 311, 51))
        self.lineEdit_5.setToolTipDuration(-1)
        self.lineEdit_5.setStyleSheet("QLineEdit {\n"
"    border-radius: 10px;\n"
"       font: 18pt \"Fredoka One Light\";\n"
"    color: rgb(255, 255, 255);\n"
"    border: 2px solid rgb(160,160,160);\n"
"    padding: 5px;\n"
"    selection-color: rgb(0, 0, 255);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(0, 153, 188);\n"
"}\n"
"")
        self.lineEdit_5.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(330, 20, 131, 51))
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"font: 18pt \"Fredoka One \";\n"
"border: 2px solid rgb(160,160,160);\n"
"padding: 5px;\n"
"border-radius: 6px;\n"
"}\n"
"QPushButton:pressed {\n"
"   \n"
"    background-color: rgb(0, 85, 255);\n"
"    \n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 90, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 467, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "Enter Amount to withdraw"))
        self.pushButton_7.setText(_translate("MainWindow", "Withdraw"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = withdraw()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())