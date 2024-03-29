import sys

from PyQt5.QtCore import QDateTime, Qt
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    """
    MainWindow class
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')
        self.resize(400, 400)

        # Create Widgets
        self.led_first_name = QLineEdit('John')
        self.led_last_name = QLineEdit('Doe')
        self.dte_started = QDateTimeEdit()
        self.spb_age = QSpinBox()
        self.btn_submit = QPushButton('Submit')

        # Setup Layout
        self.main_layout = QFormLayout()
        self.main_layout.setLabelAlignment(Qt.AlignLeft)
        self.main_layout.setRowWrapPolicy(QFormLayout.WrapAllRows)
        self.main_layout.addRow('First Name: ', self.led_first_name)
        self.main_layout.addRow('Last Name: ', self.led_last_name)
        self.main_layout.addRow('Date Started: ', self.dte_started)
        self.main_layout.addRow('Age: ', self.spb_age)
        self.main_layout.addRow('', self.btn_submit)

        self.setLayout(self.main_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = DlgMain()
    dlg.show()
    sys.exit(app.exec_())
