import sys

from PyQt5.QtGui import QColor, QFont
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    """
    MainWindow class
    """

    def __init__(self):
        super().__init__()
        self.resize(200, 200)

        self.btn = QPushButton('Choose font', self)
        self.btn.move(35, 50)
        self.btn.clicked.connect(self.btn_clicked_handler)
        font = QFont('Arial', pointSize=14, weight=75, italic=True)
        self.btn.setFont(font)

    def btn_clicked_handler(self):
        font, b_ok = QFontDialog.getFont()
        if b_ok and font:
            print(font.family())
            print(font.bold())
            print(font.weight())
            print(font.pointSize())
            self.btn.setFont(font)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = DlgMain()
    dlg.show()
    sys.exit(app.exec_())
