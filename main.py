# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from withdraw import withdraw
from deposit import deposit
from last5 import last
from profile import Profile
from update import update

class mainwin(object):
    def openwith(self):
        
        self.window = QtWidgets.QMainWindow()
        self.ui = withdraw()
        self.ui.setupUi(self.window)
        self.window.show()
    def opende(self):
        
        self.window = QtWidgets.QMainWindow()
        self.ui = deposit()
        self.ui.setupUi(self.window)
        self.window.show()
    def openlast(self):
        
        self.window = QtWidgets.QMainWindow()
        self.ui = last()
        self.ui.setupUi(self.window)
        self.window.show()
    def openprofile(self):
        
        self.window = QtWidgets.QMainWindow()
        self.ui = Profile()
        self.ui.setupUi(self.window)
        self.window.show()

    def openupdate(self):
        
        self.window = QtWidgets.QMainWindow()
        self.ui = update()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(688, 489)
        MainWindow.setStyleSheet("background-color: rgb(18, 18, 18);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 30, 251, 61))
        self.pushButton.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"font: 18pt \"Fredoka One \";\n"
"border: 2px solid rgb(160,160,160);\n"
"padding: 5px;\n"
"border-radius: 6px;\n"
"}\n"
"QPushButton:pressed {\n"
"   \n"
"    background-color: rgb(0, 85, 255);\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 140, 251, 61))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"font: 18pt \"Fredoka One \";\n"
"border: 2px solid rgb(160,160,160);\n"
"padding: 5px;\n"
"border-radius: 6px;\n"
"}\n"
"QPushButton:pressed {\n"
"   \n"
"    background-color: rgb(0, 85, 255);\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 250, 251, 61))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"font: 18pt \"Fredoka One \";\n"
"border: 2px solid rgb(160,160,160);\n"
"padding: 5px;\n"
"border-radius: 6px;\n"
"}\n"
"QPushButton:pressed {\n"
"   \n"
"    background-color: rgb(0, 85, 255);\n"
"}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(400, 140, 251, 61))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"font: 18pt \"Fredoka One \";\n"
"border: 2px solid rgb(160,160,160);\n"
"padding: 5px;\n"
"border-radius: 6px;\n"
"}\n"
"QPushButton:pressed {\n"
"   \n"
"    background-color: rgb(0, 85, 255);\n"
"}\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(400, 30, 251, 61))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"font: 18pt \"Fredoka One \";\n"
"border: 2px solid rgb(160,160,160);\n"
"padding: 5px;\n"
"border-radius: 6px;\n"
"}\n"
"QPushButton:pressed {\n"
"   \n"
"    background-color: rgb(0, 85, 255);\n"
"}\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(400, 250, 251, 61))
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(255, 0, 0);\n"
"font: 18pt \"Fredoka One \";\n"
"border: 2px solid rgb(160,160,160);\n"
"padding: 5px;\n"
"border-radius: 6px;\n"
"}\n"
"QPushButton:pressed {\n"
"   \n"
"    background-color: rgb(218, 0, 0);\n"
"}\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(220, 360, 251, 61))
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
"}\n"
"")
        self.pushButton_7.setObjectName("pushButton_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 688, 21))
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
        self.pushButton.setText(_translate("MainWindow", "Withdraw Money"))
        self.pushButton_2.setText(_translate("MainWindow", "Deposit Money"))
        self.pushButton_3.setText(_translate("MainWindow", "Last 5 Activities"))
        self.pushButton_5.setText(_translate("MainWindow", "Update Profile"))
        self.pushButton_4.setText(_translate("MainWindow", "View Profile"))
        self.pushButton_6.setText(_translate("MainWindow", "Delete Account"))
        self.pushButton_7.setText(_translate("MainWindow", "Log Out"))
        #self.pushButton.clicked.connect(self.openwith)
        #self.pushButton_2.clicked.connect(self.opende)
        #self.pushButton_3.clicked.connect(self.openlast)
        #self.pushButton_4.clicked.connect(self.openprofile)
        #self.pushButton_5.clicked.connect(self.openupdate)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = mainwin()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())