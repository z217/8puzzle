import sys

from PyQt5.QtWidgets import QApplication

from gui.Window import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    window.setMinimumSize(window.width(), window.height())
    window.setMaximumSize(window.width(), window.height())
    sys.exit(app.exec_())
