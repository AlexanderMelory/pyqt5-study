import sys

from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    """
    MainWindow class
    """

    def __init__(self):
        super().__init__()
        self.resize(1000, 1000)

        self.btn = QPushButton('Disable Label', self)
        self.btn.setIcon(QIcon('../static/toggle_on.webp'))
        self.btn.move(35, 50)
        self.btn.clicked.connect(self.btn_clicked_handler)

        self.lbl = QLabel('Label Text', self)
        self.lbl.move(35, 100)
        self.lbl.resize(500, 500)
        font = QFont('Times New Roman', 14, 75, italic=True)
        self.lbl.setFont(font)

    def btn_clicked_handler(self):
        if self.lbl.isEnabled():
            self.lbl.setDisabled(True)
            self.lbl.setText('Label is disabled')
            self.btn.setText('Enable Label')
            self.btn.setIcon(QIcon('../static/toggle_off.png'))

        else:
            self.lbl.setEnabled(True)
            self.lbl.setText('Label is enabled')
            self.btn.setText('Disable Label')
            self.btn.setIcon(QIcon('../static/toggle_on.webp'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = DlgMain()
    dlg.show()
    sys.exit(app.exec_())
