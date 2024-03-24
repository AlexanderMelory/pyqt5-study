import random
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextCursor, QColor
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    """
    MainWindow class
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')

        self.lyt_main = QVBoxLayout()
        self.setLayout(self.lyt_main)

        self.ted = QTextEdit()
        self.ted.setText('012345678901234567890123456789012345678901234567890123456789')
        self.lyt_main.addWidget(self.ted)

        self.btn_background = QPushButton('Set Red Background Color')
        self.btn_background.clicked.connect(self.btn_background_handler)

        self.btn_html = QPushButton('Add HTML')
        self.btn_html.clicked.connect(self.btn_html_handler)

        self.lyt_main.addWidget(self.btn_html)
        self.lyt_main.addWidget(self.btn_background)

        cursor_text = self.ted.textCursor()
        cursor_text.setPosition(15, QTextCursor.MoveAnchor)
        cursor_text.setPosition(25, QTextCursor.KeepAnchor)
        self.ted.setTextCursor(cursor_text)
        self.ted.setTextColor(QColor('green'))

    def btn_html_handler(self):
        html = (
            """
            <h1>Rainbow Colors</h1>
            <ul>
                <li>Red</li>
                <li><b>Bold Orange</b></li>
                <li>Yellow</li>
                <li><i>Italic Green</i></li>
                <li>Blue</li>
                <li>Indigo</li>
                <li>Violet</li>
            </ul>
            """
        )
        self.ted.setText(html)

    def btn_background_handler(self):
        color = QColorDialog.getColor(QColor('black'))
        self.ted.setTextBackgroundColor(QColor(color))
        self.ted.setFontPointSize(20)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = DlgMain()
    dlg.show()
    sys.exit(app.exec_())
