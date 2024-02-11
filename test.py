import sys
from PyQt5.QtWidgets import *


# app = QApplication(sys.argv)    # create app
# dlgMain = QDialog() # create main window
# dlgMain.setWindowTitle('First GUI')
# dlgMain.show()  # show GUI
#
# sys.exit(app.exec_()) # start app

class DlgMain(QDialog):
    """
    MainWindow class
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Second GUI')
        self.resize(300, 200)

        self.led_text = QLineEdit('Default Text', self)
        self.led_text.move(100, 50)

        self.btn_update = QPushButton('Update Window Title', self)
        self.btn_update.move(100, 100)
        self.btn_update.clicked.connect(self.btn_update_clicked_handler)

    def btn_update_clicked_handler(self):
        self.setWindowTitle(self.led_text.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = DlgMain()
    dlg.show()
    sys.exit(app.exec_())
