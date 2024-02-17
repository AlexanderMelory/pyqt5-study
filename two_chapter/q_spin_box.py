import sys

from PyQt5.QtWidgets import *


class SimpleSpinBox(QSpinBox):
    def __init__(self, parent):
        super().__init__(parent)
        self.setParent(parent)
        self.setWrapping(True)
        self.setRange(0, 1000)
        self.setSingleStep(100)
        self.setValue(100)


class SimpleDoubleSpinBox(QDoubleSpinBox):
    def __init__(self, parent):
        super().__init__(parent)
        self.setParent(parent)
        self.setDecimals(2)
        self.setSingleStep(0.01)
        self.setRange(0.4, 3)
        self.setPrefix('Height: ')
        self.setSuffix(' meters')


class DlgMain(QDialog):
    """
    MainWindow class
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')
        self.resize(400, 400)

        self.spin_box_int = SimpleSpinBox(self)
        self.spin_box_int.valueChanged.connect(self.spin_box_int_value_handler)
        self.spin_box_int.editingFinished.connect(self.spin_box_int_editing_handler)
        self.spin_box_int.move(50, 50)

        self.spin_box_double = SimpleDoubleSpinBox(self)
        self.spin_box_double.valueChanged.connect(self.spin_box_double_value_handler)
        self.spin_box_double.editingFinished.connect(self.spin_box_double_editing_handler)
        self.spin_box_double.move(50, 80)

    def spin_box_int_value_handler(self, val):
        print(val, val % 100)
        if val % 100:
            self.spin_box_int.setStyleSheet('color: red')
        else:
            self.spin_box_int.setStyleSheet('')

    def spin_box_int_editing_handler(self):
        if self.spin_box_int.value() % 100:
            QMessageBox.critical(self, 'Invalid Number', 'Invalid value was entered \n\nMust be divisible by 100')
            self.spin_box_int.setFocus()

    def spin_box_double_value_handler(self, val):
        print(self.spin_box_double.text())
        print(self.spin_box_double.value())

    def spin_box_double_editing_handler(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = DlgMain()
    dlg.show()
    sys.exit(app.exec_())
