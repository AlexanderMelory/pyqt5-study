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
        self._setup_ui()

    def _setup_ui(self):
        self.setWindowTitle('Main Window')
        self.resize(400, 600)
        self._create_widgets()
        self._setup_layout()

    def _setup_layout(self):
        self.lyt_main = QVBoxLayout()
        self.lyt_main.addWidget(self.trwQt)
        self.setLayout(self.lyt_main)

    def _create_widgets(self):
        self.trwQt = QTreeWidget()
        self.trwQt.setColumnCount(3)
        self.trwQt.itemDoubleClicked.connect(self._trw_qt_dbl_clicked_handler)
        self.trwQt.setHeaderLabels(['Qt Class', 'Methods', 'Signals'])

        self._create_top_items()

        self.trwQt.sortItems(0, Qt.AscendingOrder)
        self.trwQt.setColumnWidth(0, 200)
        self.trwQt.expandItem(self.twi_widget)

    def _create_top_items(self):
        self.twi_widget = QTreeWidgetItem(self.trwQt, ['QWidget Module'])
        self.twi_gui = QTreeWidgetItem(self.trwQt, ['QGui Module'])
        self.twi_core = QTreeWidgetItem(self.trwQt, ['QCore Module'])
        self._add_sub_items()

    def _add_sub_items(self):
        # Add subitems to QWidget module
        lst_widget = ['QDialog', 'QLabel', 'QLineEdit', 'QGroupBox', 'QFrame']
        for cls in lst_widget:
            self.twi_widget.addChild(QTreeWidgetItem([cls, str(random.randrange(25)), str(random.randrange(10))]))

        # Add subitems to QGui module
        lst_gui = ['QBitmap', 'QColor', 'QFont', 'QIcon', 'QImage']
        for cls in lst_gui:
            self.twi_gui.addChild(QTreeWidgetItem([cls, str(random.randrange(25)), str(random.randrange(10))]))

        # Add subitems to QCore module
        lst_core = ['QThread', 'QDateTime', 'QPixmap', 'QUrl', 'QFile']
        for cls in lst_core:
            self.twi_core.addChild(QTreeWidgetItem([cls, str(random.randrange(25)), str(random.randrange(10))]))

        # Add subitems to QDialog subitem
        twi_dialog_items = self.trwQt.findItems('QDialog', Qt.MatchRecursive)
        for item in twi_dialog_items:
            for cls in lst_core:
                item.addChild(QTreeWidgetItem([cls, str(random.randrange(25)), str(random.randrange(10))]))

    # Handlers
    def _trw_qt_dbl_clicked_handler(self, twi: QTreeWidgetItem, col: int):
        QMessageBox.information(self, 'Qt Classes', f'You have clicked on the {twi.text(col)} class')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = DlgMain()
    dlg.show()
    sys.exit(app.exec_())
