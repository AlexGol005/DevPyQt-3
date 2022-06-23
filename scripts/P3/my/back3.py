import os

import PySide2

from my3 import Ui_Form
from PySide2 import QtWidgets, QtGui, QtCore


class MyWindow(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

class Timer(QtCore.QThread):
    pass

class Site(QtCore.QThread):
    pass

class Sistem(QtCore.QThread):
    pass

# signals