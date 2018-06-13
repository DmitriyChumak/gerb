import sys, os
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qt import *


class MainWindow(QMainWindow):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.MenuBar()
        self.MW = MainWidget(self)
        self.setCentralWidget(self.MW)
        self.setGeometry(30, 50, 1500, 800)
        self.setWindowTitle('Panalize')
        self.show()

    def MenuBar (self):
        #Actions
        openfileAction = QAction('&Open File', self)
        openfileAction.setShortcut('Ctrl+O')
        openfileAction.setStatusTip('Open File')
        openfileAction.triggered.connect(self.showDialog)
        exitAction = QAction('&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        #menubar
        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openfileAction)
        fileMenu.addAction(exitAction)

    def showDialog(self):
        try:
         fname = QFileDialog.getOpenFileName(self, 'Open file', )[0]
         print(fname)
         with open(fname ,"r") as file:
            read_data = file.readlines()
            print(read_data)
        except Exception as eror:
            print(eror)


class MainWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.initEX()


    def initEX(self):
        MaxPanelSize= QLabel('Max Panel Size')
        PCBSize = QLabel('PCB Size')
        review = QLabel('Review')
        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setColumnStretch(0,5)
        grid.setColumnStretch(1,5)
        grid.setColumnStretch(2,5)
        grid.setColumnStretch(3,5)
        grid.setColumnStretch(4,5)
        grid.setSpacing(10)


        grid.addWidget(MaxPanelSize, 1, 0)
        grid.addWidget(PCBSize, 2, 0)
        grid.addWidget(titleEdit, 2, 1)


        grid.addWidget(authorEdit, 2, 1)
        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)
        self.setLayout(grid)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())