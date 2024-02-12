import sys

from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    """
    MainWindow class
    """

    def __init__(self):
        super().__init__()
        self.resize(1000, 1000)

        self.btn = QPushButton('Change Label', self)
        self.btn.move(35, 50)
        self.btn.clicked.connect(self.btn_clicked_handler)

        self.lbl = QLabel('Label Text', self)
        self.lbl.move(35, 100)
        self.lbl.resize(500, 500)
        font = QFont('Times New Roman', 14, 75, italic=True)
        self.lbl.setFont(font)

    def btn_clicked_handler(self):
        rich_text = """
        <h1>Hello World!</h1>
        <ul>
            <li>Hello</li>
            <li>World</li>
        </ul>
        """
        self.lbl.setText(rich_text)
        px_map = QPixmap('../static/snimok.png').scaled(400, 400)
        self.lbl.setPixmap(px_map)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = DlgMain()
    dlg.show()
    sys.exit(app.exec_())
