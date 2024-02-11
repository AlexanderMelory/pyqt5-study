import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    """
    MainWindow class
    """

    def __init__(self):
        super().__init__()
        self.resize(200, 200)

        self.btn = QPushButton('Show message', self)
        self.btn.move(35, 50)
        self.btn.clicked.connect(self.btn_clicked_handler)

    def btn_clicked_handler(self):
        # result = QMessageBox.question(self, 'Disk Full', 'Your disk drive is almost full')
        # if result == QMessageBox.Yes:
        #     QMessageBox.information(self, '', 'You`ve clicked "Yes" button')
        # elif result == QMessageBox.No:
        #     QMessageBox.information(self, '', 'You`ve clicked "No" button')
        msgDiskFull = QMessageBox()
        msgDiskFull.setWindowTitle('Full Drive')
        msgDiskFull.setText('Your hard drive is almost full')
        msgDiskFull.setDetailedText('Please free up disk space')
        msgDiskFull.setIcon(QMessageBox.Information)
        msgDiskFull.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msgDiskFull.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = DlgMain()
    dlg.show()
    sys.exit(app.exec_())
