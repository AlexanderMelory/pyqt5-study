import sys

from PyQt5.QtCore import QDate, QTime, QDateTime
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    """
    MainWindow class
    """

    def __init__(self):
        super().__init__()
        self.resize(200, 200)

        self.btn = QPushButton('Dates', self)
        self.btn.move(35, 50)
        self.btn.clicked.connect(self.btn_clicked_handler)

    def btn_clicked_handler(self):
        date = QDate.currentDate()
        print(date.toString())
        print(date.toJulianDay())
        print(date.dayOfWeek())
        print(date.dayOfYear())
        print(date.addDays(21).toString())

        time = QTime(13, 20)
        time2 = QTime(15, 20)
        print(time.toString())
        print(time.secsTo(time2))

        datetime_ = QDateTime.currentDateTime()
        print(datetime_.toString())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = DlgMain()
    dlg.show()
    sys.exit(app.exec_())
