import sys
from PyQt5.QtWidgets import *


app = QApplication(sys.argv)    # create app
dlgMain = QDialog() # create main window
dlgMain.setWindowTitle('First GUI')
dlgMain.show()  # show GUI

app.exec_() # start app