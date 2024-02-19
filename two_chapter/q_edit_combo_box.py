import sys

from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    """
    MainWindow class
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')
        self.resize(400, 400)

        self.combo_box = QComboBox(self)
        self.combo_box.addItem('Alabama', 'AL')
        self.combo_box.addItem('Alaska', 'AR')
        self.combo_box.addItem('Minnesota', 'MA')
        self.combo_box.addItem('Missouri', 'MO')
        self.combo_box.addItem('Michigan', 'MI')
        self.combo_box.currentIndexChanged.connect(self.combo_box_index_handler)
        self.combo_box.highlighted.connect(self.combo_box_highlight_handler)
        self.combo_box.move(50, 50)

        self.combo_box_posts = QComboBox(self)
        self.combo_box_posts.setEditable(True)
        self.combo_box_posts.setDuplicatesEnabled(False)
        self.combo_box_posts.addItem('First Post', 'simple text 1')
        self.combo_box_posts.addItem('Second Post', 'simple text 2')
        self.combo_box_posts.addItem('Third Post', 'simple text 3')
        self.combo_box_posts.addItem('Fourth Post', 'simple text 4')
        self.combo_box_posts.currentIndexChanged.connect(self.combo_box_posts_index_handler)
        self.combo_box_posts.resize(150, 25)
        self.combo_box_posts.move(50, 90)

        self.lbl_abbreviation = QLabel(
            f'State Abbreviation: {self.combo_box.itemData(self.combo_box.currentIndex())}', self
        )
        self.lbl_abbreviation.resize(150, 30)
        self.lbl_abbreviation.move(170, 50)

    def combo_box_posts_index_handler(self, idx):
        if not self.combo_box_posts.itemData(idx):
            input_str, b_ok = QInputDialog.getText(
                self, 'New Post', f'Enter your nickname for {self.combo_box_posts.itemText(idx)}'
            )
            if b_ok:
                self.combo_box_posts.setItemData(idx, input_str)

        QMessageBox.information(self, 'Posts', f'You have selected {self.combo_box_posts.itemData(idx)}')

    def combo_box_highlight_handler(self, idx):
        self.lbl_abbreviation.setText(f'State Abbreviation: {self.combo_box.itemData(idx)}')

    def combo_box_index_handler(self, idx):
        QMessageBox.information(self, 'Combo box index', f'You chose {self.combo_box.itemData(idx)}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = DlgMain()
    dlg.show()
    sys.exit(app.exec_())
