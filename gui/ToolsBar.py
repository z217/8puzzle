from PyQt5 import QtGui
from PyQt5.QtCore import QObject, pyqtSignal, Qt
from PyQt5.QtWidgets import *

from gui.Table import Table
from astar.Astar import *


class ToolsBar(QWidget):
    def __init__(self, table: Table):
        super(ToolsBar, self).__init__()
        self.table = table
        self.n = 4
        self.settingButton = QPushButton('设置')
        self.edit = QLineEdit()
        self.edit.setValidator(QtGui.QIntValidator())
        self.edit.setText('4')
        self.layout = QHBoxLayout()
        self.nSetter = QWidget()
        self.startButton = QPushButton('开始')
        self.showMessage = ShowMessage()
        self.startButton.clicked.connect(self.startEvent)

        self.initNSetter()

        self.layout.addWidget(self.nSetter)
        self.layout.addWidget(self.startButton)
        self.setLayout(self.layout)

    def initNSetter(self):
        layout = QHBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.settingButton)
        self.settingButton.clicked.connect(self.setNEvent)
        self.nSetter.setLayout(layout)

    def setNEvent(self):
        self.n = int(self.edit.text())
        if self.n < 2:
            self.n = 3
        self.table.arrange(self.n)

    def startEvent(self):
        start, end = [], []
        i, j = 0, 0
        cx, cy = -1, -1
        max = self.n * self.n
        self.settingButton.setFocusPolicy(Qt.NoFocus)
        for v in self.table.numbers:
            v.setFocusPolicy(Qt.NoFocus)
            if j == 0:
                start.append([])
                end.append([])
            if v.text() == '':
                start[-1].append(0)
            elif int(v.text()) < 0 or int(v.text()) >= max:
                self.showMessage.wrongInput.emit()
                self.table.arrange(self.n)
                return
            else:
                start[-1].append(int(v.text()))
            end[-1].append(i * self.n + j + 1)
            if v.text() == "0":
                v.setText("")
                cx, cy = i, j
            j += 1
            if j == self.n:
                i += 1
                j = 0
        end[-1][-1] = 0
        step = AStar(start, end)
        if step == -1:
            self.showMessage.noSolution.emit()
            self.table.arrange(self.n)
            return
        outExchangPath(path[-1].pID, len(path) - 1, step, cx, cy)
        self.table.playMoveAnimation(solution)


class ShowMessage(QObject):
    noSolution = pyqtSignal()
    wrongInput = pyqtSignal()
