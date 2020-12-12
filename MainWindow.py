from PySide2.QtWidgets import QWidget,QGridLayout,QVBoxLayout,QGroupBox,QPushButton
from PySide2.QtGui import QIcon,QPalette,QColor,QFont
from PySide2.QtCore import Qt
from PySide2 import QtGui
from TINY_editor import TINY_Editor
from Scanner_Output import Scanner_Output

class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()

        # set title  and geometry for the window
        self.setWindowTitle("TINY Scanner")
        self.setGeometry(800,600,400,200)

        # give orange background to the window
        # palette = self.palette()
        # palette.setColor(QPalette.Window, QColor(0, 0, 0))
        # self.setPalette(palette)
        # self.setAutoFillBackground(True)

        # set minimum width and height for the window
        self.setMinimumHeight(600)
        self.setMinimumWidth(800)
        self.setMaximumHeight(1000)
        self.setMaximumWidth(1200)

        self.center()

        # setup the grid layout design and components
        self.create_grid()
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.gpIn)
        self.vbox.addWidget(self.gpOut)
        self.vbox.setAlignment(Qt.AlignCenter | Qt.AlignTop)
        self.setLayout(self.vbox)

    def create_grid(self):
        # make group box with headline then add the gridlayout to it
        self.gpIn = QGroupBox("TINY Language")
        self.gpIn.setFont(QFont("Helvetica", 12))
        self.gpOut = QGroupBox("Scanner Output")
        self.gpOut.setFont(QFont("Helvetica", 12))

        # create gridlayout with spacing between columns and rows
        glIn = QGridLayout()
        glIn.setSpacing(10)
        glOut = QGridLayout()
        glOut.setSpacing(10)

        self.editor = TINY_Editor(self)

        self.scanner_out = Scanner_Output(self)
        palette = self.palette()
        palette.setColor(QPalette.Active,QPalette.Base,QColor(150,150,150))
        self.scanner_out.setPalette(palette)
        self.scanner_out.setAutoFillBackground(True)

        self.runButton = QPushButton("Scan")
        self.runButton.setIcon(QIcon("icons/run.png"))
        self.runButton.setMaximumWidth(100)
        self.runButton.setMaximumHeight(30)

        glIn.addWidget(self.editor, 0, 0)
        glIn.addWidget(self.runButton, 1, 0)
        glOut.addWidget(self.scanner_out, 0, 0)

        self.gpIn.setLayout(glIn)
        self.gpOut.setLayout(glOut)

    # to center the application window at the beginning
    def center(self):
        qRect = self.frameGeometry()
        centerPoint = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())
