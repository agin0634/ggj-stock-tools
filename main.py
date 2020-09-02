import os
import sys
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from ui_main import Ui_MainWindow
from ui_splashScreen import Ui_SplashScreen
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow

from app_modules import *

# GLOBALS
counter = 0

class AppWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        UIFunctions.uiDefinitions(self)
        

class SplashWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.timer = QTimer(self)
        self.timer.start(35)
        self.timer.timeout.connect(self.progress)
        self.show()
    
    def progress(self):
        global counter
        self.ui.progressBar.setValue(counter)

        if counter > 97:
            self.timer.stop()
            self.main = AppWindow()
            self.main.show()
            self.close()
        counter += 10 # TODO debugging


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = SplashWindow()
    sys.exit(app.exec_())