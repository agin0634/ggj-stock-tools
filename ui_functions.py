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
            GLOBAL_STATE = 0
            self.showNormal()

    def uiDefinitions(self):

        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())
        self.ui.btn_maximize.clicked.connect(lambda: UIFunctions.maximize_restore(self))
        self.ui.btn_close.clicked.connect(lambda: self.close())