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
        result = QFileDialog.getOpenFileName(self, 'Open file', '/static/', 'PNG File (*.png);;JPEG File (*.jpeg)')
        print(result)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = DlgMain()
    dlg.show()
    sys.exit(app.exec_())
