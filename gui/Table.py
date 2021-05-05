from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, QSequentialAnimationGroup, QParallelAnimationGroup
from PyQt5.QtWidgets import QWidget, QGridLayout

from gui.NumberEdit import NumberEdit


class Table(QWidget):
    def __init__(self, mainWindow: QWidget, n: int):
        super(Table, self).__init__()
        self.setParent(mainWindow)
        self.numberMap = {}
        self.geometrys = {}
        self.numbers = []
        self.n = n
        self.layout = QGridLayout()
        self.animationGroup = QSequentialAnimationGroup()
        self.setLayout(self.layout)
        self.arrange(n)

    def arrange(self, n: int):
        self.n = n
        self.animationGroup.clear()
        for i in range(len(self.numbers) - 1, -1, -1):
            self.layout.removeWidget(self.numbers[i])
            self.numbers[i].deleteLater()
        self.numbers.clear()
        for i in range(n):
            for j in range(n):
                self.numbers.append(NumberEdit(i * n + j + 1))
                self.layout.addWidget(self.numbers[-1], i, j)
        self.numbers[-1].setText('0')
        self.setMinimumSize(0, 0)

    def playMoveAnimation(self, solution: list[int]):
        self.numberMap.clear()
        self.geometrys.clear()
        self.setMinimumSize(self.width(), self.height())
        space = None
        for number in self.numbers:
            if number.text() == "":
                space = number
                self.geometrys[0] = space.geometry()
            else:
                self.numberMap[int(number.text())] = number
                self.geometrys[int(number.text())] = number.geometry()
            self.layout.removeWidget(number)

        for i in solution:
            number = self.numberMap[i]
            animation1 = QPropertyAnimation(number, b"geometry")
            animation1.setDuration(1000)
            animation1.setStartValue(self.geometrys[i])
            animation1.setEndValue(self.geometrys[0])
            animation1.setEasingCurve(QEasingCurve.InOutQuad)
            animation2 = QPropertyAnimation(space, b"geometry")
            animation2.setDuration(1000)
            animation2.setStartValue(self.geometrys[0])
            animation2.setEndValue(self.geometrys[i])
            animation2.setEasingCurve(QEasingCurve.InOutQuad)
            parallelAnimation = QParallelAnimationGroup()
            parallelAnimation.addAnimation(animation1)
            parallelAnimation.addAnimation(animation2)
            self.animationGroup.addAnimation(parallelAnimation)
            self.geometrys[0], self.geometrys[i] = self.geometrys[i], self.geometrys[0]
        self.animationGroup.finished.connect(lambda: self.arrange(self.n))
        self.animationGroup.start()
