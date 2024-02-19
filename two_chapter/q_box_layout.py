import sys
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
        self.lbl_1 = QLabel('Label 1')
        self.btn_2 = QPushButton('Button 2')
        self.line_edit_3 = QLineEdit('Line Edit 3')
        self.cmb_4 = QComboBox()
        self.cmb_4.addItems(['Item 1', 'Item 2', 'Item 3', 'Item 4'])

        # Setup Layout
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.lbl_1)
        self.main_layout.addWidget(self.btn_2)
        self.main_layout.addStretch()
        self.main_layout.addWidget(self.line_edit_3)
        self.main_layout.addWidget(self.cmb_4)

        self.setLayout(self.main_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = DlgMain()
    dlg.show()
    sys.exit(app.exec_())
