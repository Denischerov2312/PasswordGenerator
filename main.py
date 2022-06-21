from design import UiMainwindow
from PyQt5 import QtWidgets
import sys


def start():
    application = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = UiMainwindow()
    ui.setupUi(main_window)
    ui.add_function()
    main_window.show()
    sys.exit(application.exec_())


if __name__ == '__main__':
    start()
