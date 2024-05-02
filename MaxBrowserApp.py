import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1218, 836)
        MainWindow.setWindowTitle("")
        MainWindow.setStyleSheet("QWidget#widget{\n"
"    border: 4px solid rgb(45, 45, 45);\n"
"    border-radius: 20px;\n"
"}")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setStyleSheet("background-color: rgb(20, 20, 20);\n"
"\n"
"")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 80))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 120))
        self.widget_2.setBaseSize(QtCore.QSize(0, 80))
        self.widget_2.setStyleSheet("QWidget#widget_2{\n"
"    background-color: rgb(20, 20, 20);\n"
"    border-top-left-radius: 20px;\n"
"    border-top-right-radius: 20px;\n"
"}\n"
"QPushButton{\n"
"    background-color: rgba(0,0,0,0);\n"
"    color: rgb(144,144,144);\n"
"    font: bold;\n"
"    font-size: 15px;\n"
"    font-family: Arial;\n"
"}\n"
"QPushButton:hover{\n"
"    color: rgb(66, 157, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top: 5px;\n"
"    padding-left: 5px;\n"
"    color: rgb(91, 88, 53);\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setContentsMargins(12, -1, 12, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setMinimumSize(QtCore.QSize(15, 15))
        self.label_6.setMaximumSize(QtCore.QSize(20, 20))
        self.label_6.setStyleSheet("background-color: rgb(66, 157, 255);\n"
"border-radius: 7px;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setMinimumSize(QtCore.QSize(20, 20))
        self.label_5.setMaximumSize(QtCore.QSize(20, 20))
        self.label_5.setStyleSheet("background-color: rgb(66, 157, 255);\n"
"border-radius: 7px;")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setMaximumSize(QtCore.QSize(20, 20))
        self.label_4.setStyleSheet("background-color: rgb(66, 157, 255);\n"
"border-radius: 7px;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setMinimumSize(QtCore.QSize(200, 0))
        self.label_3.setStyleSheet("color: rgb(144,144,144);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.Minimize_Button = QtWidgets.QPushButton(self.widget_2)
        self.Minimize_Button.setMinimumSize(QtCore.QSize(30, 30))
        self.Minimize_Button.setMaximumSize(QtCore.QSize(30, 30))
        self.Minimize_Button.setObjectName("Minimize_Button")
        self.horizontalLayout.addWidget(self.Minimize_Button)
        self.Maximize_Button = QtWidgets.QPushButton(self.widget_2)
        self.Maximize_Button.setMinimumSize(QtCore.QSize(30, 30))
        self.Maximize_Button.setMaximumSize(QtCore.QSize(30, 30))
        self.Maximize_Button.setCheckable(True)
        self.Maximize_Button.setObjectName("Maximize_Button")
        self.horizontalLayout.addWidget(self.Maximize_Button)
        self.Close_Button = QtWidgets.QPushButton(self.widget_2)
        self.Close_Button.setMinimumSize(QtCore.QSize(30, 30))
        self.Close_Button.setMaximumSize(QtCore.QSize(30, 30))
        self.Close_Button.setObjectName("Close_Button")
        self.horizontalLayout.addWidget(self.Close_Button)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Back_Button = QtWidgets.QPushButton(self.widget_2)
        self.Back_Button.setMinimumSize(QtCore.QSize(40, 30))
        self.Back_Button.setMaximumSize(QtCore.QSize(40, 30))
        self.Back_Button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/BrowserImages/arrow (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Back_Button.setIcon(icon)
        self.Back_Button.setIconSize(QtCore.QSize(25, 25))
        self.Back_Button.setObjectName("Back_Button")
        self.horizontalLayout_2.addWidget(self.Back_Button)
        self.Forward_Button = QtWidgets.QPushButton(self.widget_2)
        self.Forward_Button.setMinimumSize(QtCore.QSize(40, 30))
        self.Forward_Button.setMaximumSize(QtCore.QSize(40, 30))
        self.Forward_Button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/BrowserImages/right-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Forward_Button.setIcon(icon1)
        self.Forward_Button.setIconSize(QtCore.QSize(40, 40))
        self.Forward_Button.setObjectName("Forward_Button")
        self.horizontalLayout_2.addWidget(self.Forward_Button)
        self.Refresh_Button = QtWidgets.QPushButton(self.widget_2)
        self.Refresh_Button.setMinimumSize(QtCore.QSize(40, 30))
        self.Refresh_Button.setMaximumSize(QtCore.QSize(40, 30))
        self.Refresh_Button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/BrowserImages/refresh-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Refresh_Button.setIcon(icon2)
        self.Refresh_Button.setIconSize(QtCore.QSize(30, 30))
        self.Refresh_Button.setObjectName("Refresh_Button")
        self.horizontalLayout_2.addWidget(self.Refresh_Button)
        self.Search_bar = QtWidgets.QLineEdit(self.widget_2)
        self.Search_bar.setMinimumSize(QtCore.QSize(25, 25))
        self.Search_bar.setMaximumSize(QtCore.QSize(16777215, 35))
        self.Search_bar.setStyleSheet("background-color: rgb(31, 31, 3);\n"
"border-radius: 6px;\n"
"color: rgb(144, 144, 144);\n"
"padding-left: 5px;\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"")
        self.Search_bar.setObjectName("Search_bar")
        self.horizontalLayout_2.addWidget(self.Search_bar)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.webEngineView = QWebEngineView(self.widget)
        self.webEngineView.page().setBackgroundColor(QtGui.QColor(45, 45, 45, 255))
        self.webEngineView.setObjectName("webEngineView")
        self.verticalLayout_2.addWidget(self.webEngineView)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 20))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_2.setStyleSheet("background-color: rgb(45, 45, 45);\n"
"border-bottom-left-radius: 20px;\n"
"border-bottom-right-radius: 20px;\n"
"color: rgb(144, 144, 144);\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.verticalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.label_3.setText(_translate("MainWindow", "Maximus Browser"))
        self.Minimize_Button.setText(_translate("MainWindow", "–"))
        self.Maximize_Button.setText(_translate("MainWindow", "⃣"))
        self.Close_Button.setText(_translate("MainWindow", "X"))
        self.label_2.setText(_translate("MainWindow", "Developed by Maximus ©"))

import BrowserImages





    
