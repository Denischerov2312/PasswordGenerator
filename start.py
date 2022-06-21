from ButtonControl import UiMainwindow
import sys
from PyQt5 import QtWidgets
from design import UiMainwindow
from ButtonControl import ButtonControl


class ProgramStart:
    def __init__(self):
        self.application = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = UiMainwindow()

    def start(self):
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        sys.exit(self.application.exec_())
