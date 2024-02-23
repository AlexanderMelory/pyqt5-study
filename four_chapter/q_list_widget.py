import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    """
    MainWindow class
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')
        self.resize(400, 200)
        self._setup_ui()

    def _setup_ui(self):
        self._create_widgets()
        self._setup_layout()

    def _create_widgets(self):
        self.lwg_programming_topics = QListWidget()
        self.lwg_programming_topics.addItems(['Python', 'JavaScript', 'TypeScript', 'Java', 'HTML', 'CSS', 'SQL'])
        self.lwg_programming_topics.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.lwg_programming_topics.itemSelectionChanged.connect(self._topics_select_changed_handler)
        self.lwg_programming_topics.sortItems()

        self.lwg_programming_topics_selected = QListWidget()
        self.lwg_programming_topics_selected.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.lwg_programming_topics_selected.itemSelectionChanged.connect(self._topics_selected_select_changed_handler)

        self.btn_add = QPushButton('')
        self.btn_add.setIcon(QIcon('../static/arrow_right.png'))
        self.btn_add.clicked.connect(self._btn_add_clicked_handler)

        self.btn_remove = QPushButton('')
        self.btn_remove.setIcon(QIcon('../static/arrow_left.png'))
        self.btn_remove.clicked.connect(self._btn_remove_clicked_handler)

        self.btn_enroll = QPushButton('Enroll')
        self.btn_enroll.clicked.connect(self._enroll_handler)

    def _enroll_handler(self):
        if self.lwg_programming_topics_selected:
            selected_items = (self.lwg_programming_topics_selected.item(i).text() for i in
                              range(self.lwg_programming_topics_selected.count()))
            QMessageBox.information(self, 'Enroll', f'You have already enrolled to: {", ".join(selected_items)}')
        else:
            QMessageBox.warning(self, 'Not enrolled', f'Nothing to enrolled')

    def _btn_add_clicked_handler(self):
        lst_items = self.lwg_programming_topics.selectedItems()
        for item in lst_items:
            self.lwg_programming_topics.takeItem(self.lwg_programming_topics.row(item))
            self.lwg_programming_topics_selected.addItem(item.text())
        self.btn_enroll.setDefault(True)

    def _btn_remove_clicked_handler(self):
        lst_items = self.lwg_programming_topics_selected.selectedItems()
        for item in lst_items:
            self.lwg_programming_topics_selected.takeItem(self.lwg_programming_topics_selected.row(item))
            self.lwg_programming_topics.addItem(item.text())
        self.btn_enroll.setDefault(True)

    def _topics_select_changed_handler(self):
        self.btn_add.setDefault(True)

    def _topics_selected_select_changed_handler(self):
        self.btn_remove.setDefault(True)

    def _setup_layout(self):
        self.lyt_main = QVBoxLayout()
        self.lyt_lists = QHBoxLayout()
        self.lyt_buttons = QVBoxLayout()

        self.setLayout(self.lyt_main)
        self._add_widgets_to_lyt_lists()
        self._add_widgets_to_lyt_main()
        self._add_widgets_to_lyt_buttons()

    def _add_widgets_to_lyt_lists(self):
        self.lyt_lists.addWidget(self.lwg_programming_topics)
        self.lyt_lists.addLayout(self.lyt_buttons)
        self.lyt_lists.addWidget(self.lwg_programming_topics_selected)

    def _add_widgets_to_lyt_main(self):
        self.lyt_main.addLayout(self.lyt_lists)
        self.lyt_main.addWidget(self.btn_enroll)

    def _add_widgets_to_lyt_buttons(self):
        self.lyt_buttons.addStretch()
        self.lyt_buttons.addWidget(self.btn_add)
        self.lyt_buttons.addWidget(self.btn_remove)
        self.lyt_buttons.addStretch()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = DlgMain()
    dlg.show()
    sys.exit(app.exec_())
