import random
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    """
    MainWindow class
    """

    def __init__(self):
        super().__init__()

        self.ted = QPlainTextEdit(
            """
            if __name__ == '__main__':
                app = QApplication(sys.argv)
                dlg = DlgMain()
                dlg.show()
                sys.exit(app.exec_())
            """
        )
        self.lyt_main = QVBoxLayout()
        self.lyt_main.addWidget(self.ted)
        self.setLayout(self.lyt_main)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = DlgMain()
    dlg.show()
    sys.exit(app.exec_())
