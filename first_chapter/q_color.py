import sys

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    """
    MainWindow class
    """

    def __init__(self):
        super().__init__()
        self.resize(200, 200)

        self.btn = QPushButton('Choose color', self)
        self.btn.move(35, 50)
        self.btn.clicked.connect(self.btn_clicked_handler)

    def btn_clicked_handler(self):
        color = QColorDialog.getColor(QColor(0, 0, 255, 255), self, 'Choose color')
        print(color)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = DlgMain()
    dlg.show()
    sys.exit(app.exec_())
