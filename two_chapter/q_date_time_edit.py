import sys

from PyQt5.QtCore import QDateTime, QDate, QTime
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    """
    MainWindow class
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')
        self.resize(400, 400)

        self.dte_date = QDateTimeEdit(QDate().currentDate(), parent=self)
        self.dte_date.setCalendarPopup(True)
        self.dte_date.move(50, 50)

        self.dte_time = QDateTimeEdit(QTime().currentTime(), parent=self)
        self.dte_time.move(50, 80)

        self.dte_date_time = QDateTimeEdit(QDateTime.currentDateTime(), parent=self)
        self.dte_date_time.setCalendarPopup(True)
        self.dte_date_time.move(50, 110)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = DlgMain()
    dlg.show()
    sys.exit(app.exec_())
