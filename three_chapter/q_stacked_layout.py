import sys

from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    """
    MainWindow class
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')
        self.resize(400, 400)

        self.cmb_selector = QComboBox()
        self.cmb_selector.addItems(['General', 'Species', 'Location', 'Surveys'])
        self.cmb_selector.currentIndexChanged.connect(self.cmb_selector_changed_handler)

        self.wdg_general = QWidget()
        self.wdg_species = QWidget()
        self.wdg_location = QWidget()
        self.wdg_surveys = QWidget()

        # General Widgets
        self.lbl_nest_id = QLabel('24')
        self.dte_found = QDateTimeEdit(QDate(2017, 7, 11))
        self.dte_last = QDateTimeEdit(QDate(2024, 2, 19))
        self.chk_active = QCheckBox()

        # Species Widgets
        self.cmb_species = QComboBox()
        self.cmb_species.addItem('Rhesus macaque', 123)
        self.cmb_species.addItem('Emperor tamarin', 321)
        self.cmb_species.addItem('Other', 333)

        self.led_species = QLineEdit()
        self.spb_codes = QSpinBox()
        self.spb_codes.setValue(123)

        # Location Widgets
        self.spb_double_latitude = QDoubleSpinBox()
        self.spb_double_longitude = QDoubleSpinBox()

        # Survey Widgets
        self.lst_surveys = QListWidget()
        self.lst_surveys.addItem('02/25/2020 - INACTIVE')
        self.lst_surveys.addItem('03/21/2021 - ACTIVE')
        self.lst_surveys.addItem('04/15/2020 - INACTIVE')
        self.lst_surveys.addItem('06/10/2019 - INACTIVE')
        self.lst_surveys.addItem('02/02/2024 - ACTIVE')
        self.btn_add_survey = QPushButton('Add Survey')

        self.setup_layout()

    def setup_layout(self):
        # Setup main layout
        self.main_layout = QHBoxLayout()
        self.left_layout = QVBoxLayout()
        self.right_layout = QStackedLayout()

        self.main_layout.addLayout(self.left_layout)
        self.main_layout.addLayout(self.right_layout)

        # Left Widgets
        self.left_layout.addWidget(self.cmb_selector)
        self.left_layout.addStretch()

        # Right Widgets
        self.right_layout.addWidget(self.wdg_general)
        self.right_layout.addWidget(self.wdg_species)
        self.right_layout.addWidget(self.wdg_location)
        self.right_layout.addWidget(self.wdg_surveys)

        # Setup General Widget
        self.general_layout = QFormLayout()
        self.general_layout.addRow('Nest ID', self.lbl_nest_id)
        self.general_layout.addRow('Species', self.dte_found)
        self.general_layout.addRow('Date Last', self.dte_last)
        self.general_layout.addRow('Currently Active', self.chk_active)
        self.wdg_general.setLayout(self.general_layout)

        # Setup Species Widget
        self.species_layout = QFormLayout()
        self.species_layout.addRow('Species', self.cmb_species)
        self.species_layout.addRow('Species', self.led_species)
        self.species_layout.addRow('Codes', self.spb_codes)
        self.wdg_species.setLayout(self.species_layout)

        # Setup Location Widget
        self.location_layout = QFormLayout()
        self.location_layout.addRow('Latitude', self.spb_double_latitude)
        self.location_layout.addRow('Longitude', self.spb_double_longitude)
        self.wdg_location.setLayout(self.location_layout)

        # Setup Surveys Widget
        self.surveys_layout = QFormLayout()
        self.surveys_layout.addRow(self.lst_surveys)
        self.surveys_layout.addRow(self.btn_add_survey)
        self.wdg_surveys.setLayout(self.surveys_layout)

        self.setLayout(self.main_layout)

    def cmb_selector_changed_handler(self, idx):
        self.right_layout.setCurrentIndex(idx)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = DlgMain()
    dlg.show()
    sys.exit(app.exec_())
