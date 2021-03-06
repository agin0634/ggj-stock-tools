import os
import sys
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from ui_main import Ui_MainWindow
from ui_splashScreen import Ui_SplashScreen
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QTimer, QEvent, Qt
from PyQt5.QtWidgets import *

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

        def moveWindow(event):
            if UIFunctions.returnStatus(self) == 1:
                UIFunctions.maximize_restore(self)
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.frame_titleBar_title.mouseMoveEvent = moveWindow
        UIFunctions.uiDefinitions(self)
    
    # EVENT
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def resizeEvent(self, event):
        return super(AppWindow, self).resizeEvent(event)

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