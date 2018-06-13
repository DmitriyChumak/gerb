import sys
import os
from PyQt5.QtCore import QFile, QFileInfo, Qt, QTextCodec
from PyQt5.QtGui import (QFont, QFontDatabase, QFontInfo, QIcon, QKeySequence,
                         QPixmap, QTextBlockFormat, QTextCharFormat, QTextCursor,
                         QTextDocumentWriter, QTextListFormat)
from PyQt5.QtWidgets import (QAction, QActionGroup, QApplication, QColorDialog,
                             QComboBox, QFileDialog, QFontComboBox, QMainWindow, QMenu, QMessageBox,
                             QTextEdit, QToolBar)
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter, QPrintPreviewDialog
import gui


class MainWindow(QMainWindow, gui.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.ButtonClicked)  # Создал для кнопки Calc функцию
        self.radioButton.clicked.connect(self.RadioButtonChecked)  # Создал для кнопок выбора полей отдельные функции
        self.radioButton_2.clicked.connect(self.RadioButtonChecked_2)
        self.radioButton_3.setChecked(True)  # -//-//- по умолчанию выбрано 3
        self.radioButton_3.clicked.connect(self.RadioButtonChecked_3)
        self.lineEdit.textChanged[str].connect(self.PcbSize_X)  # Для текстовых полей создал свои функции
        self.lineEdit_3.textChanged[str].connect(self.PcbSize_Y)
        self.lineEdit_2.setText("210")  # -//-//- Максимальный размер панели по умолчанию
        self.lineEdit_4.setText("297")
        self.lineEdit_2.textChanged[str].connect(self.PanelSize_X)
        self.lineEdit_4.textChanged[str].connect(self.PanelSize_Y)
        self.lineEdit_7.textChanged[str].connect(self.PcbQty_X)
        self.lineEdit_8.textChanged[str].connect(self.PcbQty_Y)
        self.lineEdit_5.textChanged[str].connect(self.Milling)
        self.lineEdit_6.textChanged[str].connect(self.FieldSize)

    def ButtonClicked(self):  # Функция по нажатию на кнопку
        print("CALC good")

    def RadioButtonChecked(self):  # Функции в зависимости от выбора полей
        print("RadioButton good")

    def RadioButtonChecked_2(self):
        print("RadioButton good_2")

    def RadioButtonChecked_3(self):
        print("RadioButton good_3")

    def PcbSize_X(self):  # Функция размера платы для тестового поля размер х
        PCBSize_x = self.lineEdit.text()
        try:
            PCBSize_x = float(PCBSize_x)
        except ValueError:
            return (print('Mistake'))
        print(PCBSize_x)

    def PcbSize_Y(self):  # Функция размера платы для тестового поля размер у
        PCBSize_y = self.lineEdit_3.text()
        try:
            PCBSize_y = float(PCBSize_y)
        except ValueError:
            return (print('Mistake'))
        print(PCBSize_y)

    def PanelSize_X(self):  # Функция размера панели для тестового поля размер х
        PanelSize_X = self.lineEdit_2.text()
        try:
            PanelSize_X = float(PanelSize_X)
        except ValueError:
            return (print('Mistake'))
        print(PanelSize_X)

    def PanelSize_Y(self):  # Функция размера панели для тестового поля размер у
        PanelSize_Y = self.lineEdit_4.text()
        try:
            PanelSize_Y = float(PanelSize_Y)
        except ValueError:
            return (print('Mistake'))
        print(PanelSize_Y)

    def PcbQty_X(self):
        PcbQ_X = self.lineEdit_7.text()
        try:
            PcbQ_X = int(PcbQ_X)
        except ValueError:
            return (print('Mistake'))
        print(PcbQ_X)

    def PcbQty_Y(self):
        PcbQ_Y = self.lineEdit_8.text()
        try:
            PcbQ_Y = int(PcbQ_Y)
        except ValueError:
            return (print('Mistake'))
        print(PcbQ_Y)

    def Milling(self):
        Mil = self.lineEdit_5.text()
        try:
            Mil = float(Mil)
        except ValueError:
            return (print('Mistake'))
        print(Mil)

    def FieldSize(self):
        Field = self.lineEdit_6.text()
        try:
            Field = float(Field)
        except ValueError:
            return (print('Mistake'))
        print(Field)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())