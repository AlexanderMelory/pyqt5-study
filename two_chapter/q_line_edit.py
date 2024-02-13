import sys

from PyQt5.QtCore import Qt
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

        self.line_edit_title = QLineEdit(self.windowTitle(), self)
        self.line_edit_title.setPlaceholderText('Enter a new window title')
        self.line_edit_title.setEchoMode(QLineEdit.Password)
        self.line_edit_title.setAlignment(Qt.AlignCenter)
        self.line_edit_title.textChanged.connect(self.line_edit_title_change_handler)
        self.line_edit_title.move(50, 50)

        self.btn_update_title = QPushButton('Update Title', self)
        self.btn_update_title.clicked.connect(self.btn_update_title_handler)
        self.btn_update_title.move(150, 100)

    def btn_update_title_handler(self):
        result = QMessageBox.question(self, 'Title Editing', f'Change the title to "{self.line_edit_title.text()}"')
        if result == QMessageBox.Yes:
            self.setWindowTitle(self.line_edit_title.text())

    def line_edit_title_change_handler(self, title):
        self.setWindowTitle(title)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = DlgMain()
    dlg.show()
    sys.exit(app.exec_())
