import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5 import QtCore
from MaxBrowserApp import Ui_MainWindow
from PyQt5.QtWebEngineWidgets import QWebEnginePage


class MaxBrowser(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MaxBrowser, self).__init__()
        self.setupUi(self)

        self.Minimize_Button.clicked.connect(self.showMinimized)
        self.Maximize_Button.clicked.connect(self.showMaximized)
        self.Close_Button.clicked.connect(sys.exit)

        self.Search_bar.returnPressed.connect(self.handleSearch)

        self.Back_Button.clicked.connect(self.Back_movement)
        self.Forward_Button.clicked.connect(self.Forward_movement)
        self.Refresh_Button.clicked.connect(self.Refresh)

        # Load Google when application starts
        self.webEngineView.load(QtCore.QUrl("https://www.google.com"))

    def handleSearch(self):
        url = QtCore.QUrl.fromUserInput(self.Search_bar.text())
        if url.isValid():
            self.webEngineView.load(url)

    def Back_movement(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Back)

    def Forward_movement(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Forward)
    def Refresh(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Reload)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    borwserapp = MaxBrowser()
    maxbrowser = Ui_MainWindow()
    borwserapp.show()
    sys.exit(app.exec_())

