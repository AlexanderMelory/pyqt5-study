import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    """
    MainWindow class
    """

    def __init__(self):
        super().__init__()
        self.resize(500, 500)

        self.check_enabled = QCheckBox('Enabled', self)
        self.check_enabled.setChecked(True)
        self.check_enabled.toggled.connect(self.check_enabled_toggled_handler)
        self.check_enabled.move(50, 50)

        self.check_three_states = QCheckBox('3 state checkbox', self)
        self.check_three_states.setTristate(True)
        self.check_three_states.stateChanged.connect(self.check_three_states_handler)
        self.check_three_states.move(50, 70)

        self.lbl = QLabel('Label Text', self)
        self.lbl.resize(320, 176)
        font = QFont('Times New Roman', 24, 75, True)
        self.lbl.setFont(font)
        self.lbl.move(60, 100)

    def check_three_states_handler(self, state):
        if state == 0:
            QMessageBox.information(self, 'State', 'Unchecked')
        if state == 1:
            QMessageBox.information(self, 'State', 'Partially checked')
        if state == 2:
            QMessageBox.information(self, 'State', 'Checked')

    def check_enabled_toggled_handler(self, is_checked: bool):
        if is_checked:
            self.lbl.setEnabled(True)
            self.lbl.setText('Enabled Label')
        else:
            self.lbl.setDisabled(True)
            self.lbl.setText('Disabled Label')

    def btn_clicked_handler(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = DlgMain()
    dlg.show()
    sys.exit(app.exec_())
