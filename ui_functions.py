from main import *

GLOBAL_STATE = 0

class UIFunctions(AppWindow):
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == 0:
            self.showMaximized()
            GLOBAL_STATE = 1
        else:
            self.showNormal()
            GLOBAL_STATE = 0

    def returnStatus(self):
        return GLOBAL_STATE

    def uiDefinitions(self):
        # title bar double click event
        def doubleClickMaximize(event):
            if event.type() == QtCore.QEvent.MouseButtonDblClick:
                QtCore.QTimer.singleShot(100, lambda: UIFunctions.maximize_restore(self))
        self.ui.frame_titleBar_title.mouseDoubleClickEvent = doubleClickMaximize
        
        # sizegrip resize event
        self.sizegrip = QSizeGrip(self.ui.frame_bottom_sizegrip)
        self.sizegrip.setStyleSheet("width: 30px; height: 30px; padding-left:12px; margin-top:-3px;")

        # titlebar btns event
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())
        self.ui.btn_maximize.clicked.connect(lambda: UIFunctions.maximize_restore(self))
        self.ui.btn_close.clicked.connect(lambda: self.close())