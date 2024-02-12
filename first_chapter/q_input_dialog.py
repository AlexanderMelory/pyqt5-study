import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    """
    MainWindow class
    """

    def __init__(self):
        super().__init__()
        self.resize(200, 200)

        self.btn = QPushButton('Show input', self)
        self.btn.move(35, 50)
        self.btn.clicked.connect(self.btn_clicked_handler)

    def btn_clicked_handler(self):
        # s_name, b_ok = QInputDialog.getText(self, 'title', 'Enter your name')
        # if b_ok and s_name:
        #     QMessageBox.information(self, '', f'Your name is {s_name}')
        # else:
        #     QMessageBox.critical(self, '', 'Something was wrong')
        colors = ['red', 'green', 'blue', 'indigo', 'violet', 'yellow']
        s_color, b_ok = QInputDialog.getItem(self, '', 'Enter your color: ', colors)
        if b_ok and colors:
            QMessageBox.information(self, '', f'Your favorite color: {s_color}')
        else:
            QMessageBox.critical(self, '', 'Something was wrong')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = DlgMain()
    dlg.show()
    sys.exit(app.exec_())
