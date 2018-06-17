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
        self.pushButton.clicked.connect(self.ButtonClicked)           # Создал для кнопки Calc функцию
        self.radioButton.clicked.connect(self.RadioButtonChecked)     # Создал для кнопок выбора полей отдельные функции
        self.radioButton_2.clicked.connect(self.RadioButtonChecked_2)
        self.radioButton_3.clicked.connect(self.RadioButtonChecked_3)
        self.radioButton_3.setChecked(True)                              # -//-//- по умолчанию выбрано 3
        self.lineEdit.textChanged[str].connect(self.EditPCBSizeX)        # Для текстовых полей создал свои функции
        self.lineEdit_3.textChanged[str].connect(self.EditPCBSizeY)
        self.lineEdit_2.textChanged[str].connect(self.EditPanelSizeX)
        self.lineEdit_4.textChanged[str].connect(self.EditPanelSizeY)
        self.lineEdit_2.setText("210")                                # -//-//- Максимальный размер панели по умолчанию
        self.lineEdit_4.setText("297")
        self.lineEdit_7.textChanged[str].connect(self.PCBQty_X)
        self.lineEdit_8.textChanged[str].connect(self.PCBQty_Y)
        self.lineEdit_5.textChanged[str].connect(self.Milling)
        self.lineEdit_6.textChanged[str].connect(self.FieldSize)
        self.lineEdit_6.setText("7")


    def ButtonClicked(self, Calcx):                                          # Функция по нажатию на кнопку

        try:
            Calcx = self.PCBSize_x*self.PcbQ_X+self.Mil*(self.PcbQ_X-1)
            print(Calcx)
        except Exception as e:
            return str(e)
        print("CALC good")
        self.lineEdit_2.setText(str(Calcx))
        print(Calcx)


    def RadioButtonChecked(self):                                     # Функции в зависимости от выбора полей
        print("RadioButton good")

    def RadioButtonChecked_2(self):
        print("RadioButton good_2")

    def RadioButtonChecked_3(self):
        print("RadioButton good_3")


    def EditPCBSizeX(self, PCBSize_x):                                            # Функция размера платы для тестового поля размер х
        self.PCBSize_x = self.lineEdit.text()
        try:
            self.PCBSize_x = float(self.PCBSize_x)
        except ValueError:
            return (print('Mistake, set numbers'))
        return self.PCBSize_x


    def EditPCBSizeY(self, PCBSize_y):                                            # Функция размера платы для тестового поля размер у
        self.PCBSize_y = self.lineEdit_3.text()
        try:
            self.PCBSize_y = float(self.PCBSize_y)
        except ValueError:
            return (print('Mistake, set numbers'))
        return self.PCBSize_y


    def EditPanelSizeX(self, PanelSize_x):                                          # Функция размера панели для тестового поля размер х
        self.PanelSize_x = self.lineEdit_2.text()
        try:
            self.PanelSize_x = float(self.PanelSize_x)
        except ValueError:
            return (print('Mistake, set numbers'))
        return self.PanelSize_x


    def EditPanelSizeY(self, PanelSize_y):                                          # Функция размера панели для тестового поля размер у
        self.PanelSize_y = self.lineEdit_4.text()
        try:
            self.PanelSize_y = float(self.PanelSize_y)
        except ValueError:
            return (print('Mistake, set numbers'))
        return self.PanelSize_y


    def PCBQty_X(self, PcbQ_X):
        self.PcbQ_X = self.lineEdit_7.text()
        try:
            self.PcbQ_X = int(self.PcbQ_X)
        except ValueError:
            return (print('Mistake, set numbers'))
        return self.PcbQ_X


    def PCBQty_Y(self, PcbQ_Y):
        self.PcbQ_Y = self.lineEdit_8.text()
        try:
            self.PcbQ_Y = int(self.PcbQ_Y)
        except ValueError:
            return (print('Mistake, set numbers'))
        return self.PcbQ_Y


    def Milling(self, Mil):
        self.Mil = self.lineEdit_5.text()
        try:
            self.Mil = float(self.Mil)
        except ValueError:
            return (print('Mistake, set numbers'))
        return self.Mil


    def FieldSize(self, Field):
        self.Field = self.lineEdit_6.text()
        try:
            self.Field = float(self.Field)
        except ValueError:
            return (print('Mistake, set numbers'))
        return self.Field


    def Calc(self, CalcPCBSizeX):
        if self.PCBSize_x != 0:
            try:
                self.CalcPCBSizeX = self.PCBSize_x*self.PcbQ_X+self.Mil*(self.PcbQ_X-1)
                print(self.CalcPCBSizeX)
            except Exception as e:
                return str(e)
            print(self.CalcPCBSizeX)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())