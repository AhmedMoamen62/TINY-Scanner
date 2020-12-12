from PySide2.QtWidgets import QWidget, QGridLayout
from PySide2.QtGui import QPalette,QColor
from PySide2 import QtGui
from TINY_editor import TINY_Editor

class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()

        # set title  and geometry for the window
        self.setWindowTitle("TINY Scanner")
        self.showMaximized()

        # give orange background to the window
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(0, 0, 0))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

        self.center()

        self.create_grid()

    def create_grid(self):
        grid = QGridLayout()

        self.editor = TINY_Editor(self)

        grid.addWidget(self.editor, 0, 0)

        self.setLayout(grid)

    # to center the application window at the beginning
    def center(self):
        qRect = self.frameGeometry()
        centerPoint = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())
