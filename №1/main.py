import sys
import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from currency_converter import CurrencyConverter
from ui import Ui_MainWindow


class CurrencyConv(QtWidgets.QMainWindow):
    def __init__(self):
        super(CurrencyConv, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
    def init_UI(self):
        self.setWindowTitle('Конвертер скорости')
        self.setWindowIcon(QIcon('speed.png'))
        self.ui.pushButton.clicked.connect(self.converter)
    def converter(self):
        c = CurrencyConverter()
        input_edinitsi = self.ui.input_edinitsi.text()
        output_edinitsi = self.ui.output_edinitsi.text()
        input_chislo = int(self.ui.input_chislo.text())
        if input_edinitsi=="км/час" and output_edinitsi=="м/с":
            output_chislo = input_chislo/3.6
        elif input_edinitsi=="м/с" and output_edinitsi=="км/час":
            output_chislo = input_chislo * 3.6
        elif input_edinitsi=="км/час" and output_edinitsi=="м/час":
            output_chislo = input_chislo * 1000
        elif input_edinitsi == "м/час" and output_edinitsi == "км/час":
            output_chislo = input_chislo / 1000
        self.ui.lineEdit_4.setText(str(output_chislo))


app = PyQt5.QtWidgets.QApplication([])
application = CurrencyConv()
application.show()
sys.exit(app.exec())

self.ui.input_edinitsi.setPlaceholderText('Единицы измерения')
self.ui.input_chislo.setPlaceholderText('Сколько')
self.ui.output_edinitsi.setPlaceholderText('В единицы измерения')
self.ui.output_chislo.setPlaceholderText('Итог')

