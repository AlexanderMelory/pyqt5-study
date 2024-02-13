import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    """
    MainWindow class
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')
        self.resize(400, 200)

        self.lbl = QLabel('Label Text', self)
        self.lbl.setStyleSheet('color: red; font-size: 10px')
        self.lbl.resize(100, 300)
        self.lbl.move(50, 20)

        self.button_color_group = QButtonGroup()
        self.radio_button_red = QRadioButton('Red', self)
        self.button_color_group.addButton(self.radio_button_red)
        self.radio_button_red.setChecked(True)
        self.radio_button_red.clicked.connect(self.radio_button_color_size_handler)
        self.radio_button_red.move(50, 70)

        self.radio_button_green = QRadioButton('Green', self)
        self.button_color_group.addButton(self.radio_button_green)
        self.radio_button_green.clicked.connect(self.radio_button_color_size_handler)
        self.radio_button_green.move(50, 100)

        self.radio_button_blue = QRadioButton('Blue', self)
        self.button_color_group.addButton(self.radio_button_blue)
        self.radio_button_blue.clicked.connect(self.radio_button_color_size_handler)
        self.radio_button_blue.move(50, 130)

        self.button_size_group = QButtonGroup()
        self.radio_button_small = QRadioButton('Small Text', self)
        self.button_size_group.addButton(self.radio_button_small, 10)
        self.radio_button_small.setChecked(True)
        self.radio_button_small.clicked.connect(self.radio_button_color_size_handler)
        self.radio_button_small.move(150, 70)

        self.radio_button_medium = QRadioButton('Medium Text', self)
        self.button_size_group.addButton(self.radio_button_medium, 15)
        self.radio_button_medium.clicked.connect(self.radio_button_color_size_handler)
        self.radio_button_medium.move(150, 100)

        self.radio_button_large = QRadioButton('Large Text', self)
        self.button_size_group.addButton(self.radio_button_large, 20)
        self.radio_button_large.clicked.connect(self.radio_button_color_size_handler)
        self.radio_button_large.move(150, 130)

    def radio_button_color_size_handler(self):
        checked_color = self.button_color_group.checkedButton()
        checked_size_id = self.button_size_group.checkedId()
        self.lbl.setStyleSheet(f'color: {checked_color.text()}; font-size: {str(checked_size_id)}px')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = DlgMain()
    dlg.show()
    sys.exit(app.exec_())
