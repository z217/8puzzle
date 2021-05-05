from PyQt5.QtWidgets import QWidget, QVBoxLayout, QMessageBox

from gui.Table import Table
from gui.ToolsBar import ToolsBar


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.layout = QVBoxLayout()
        self.table = Table(self, 4)
        self.toolsBar = ToolsBar(self.table)
        self.toolsBar.showMessage.noSolution.connect(self.showNoSolutionMessage)
        self.toolsBar.showMessage.wrongInput.connect(self.showWrongInputMessage)

        self.setWindowTitle('八数码')
        self.setLayout(self.layout)
        self.resize(600, 600)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.toolsBar)
        self.layout.addWidget(self.table)

    def showNoSolutionMessage(self):
        QMessageBox.information(self, '提示', '无解', QMessageBox.Yes, QMessageBox.Yes)

    def showWrongInputMessage(self):
        QMessageBox.information(self, '提示', '不合法的输入，请检查:\n1.输入是否符合范围\n2.每个数字是否只出现一次', QMessageBox.Yes, QMessageBox.Yes)
