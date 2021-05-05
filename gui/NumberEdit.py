from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class NumberEdit(QLineEdit):

    def __init__(self, value: int):
        super(NumberEdit, self).__init__()
        self.value = value
        self.setText(str(value))
        self.setAlignment(Qt.AlignCenter)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setValidator(QtGui.QIntValidator())
        self.setStyleSheet('border-width: 1px; border-style: solid; font-size: 20px;')
