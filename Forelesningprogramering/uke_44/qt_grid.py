import sys
from PyQt6.QtWidgets import *

class Hovedvindu(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(100, 100, 700, 700)

        layout = QGridLayout()
        self.setLayout(layout)

        # Label
        min_label = QLabel("Dette er en label")
        layout.addWidget(min_label, 0, 0)

        # Knapp
        min_knapp = QPushButton("Min knapp")
        layout.addWidget(min_knapp, 0, 1)

        # Inputlinje
        min_inputlinje = QLineEdit()
        layout.addWidget(min_inputlinje, 0, 2)

        # Radioknapp
        min_radioknapp = QRadioButton("Radioknapp")
        layout.addWidget(min_radioknapp, 1, 0)

        # Sjekkboks
        min_sjekkboks = QCheckBox("Avkrysningboks")
        layout.addWidget(min_sjekkboks, 1, 1)

        # Combobox (nedtrekksmeny)
        min_combobox = QComboBox()
        min_combobox.setPlaceholderText("Velg ett av alternativene")  # Merk: "PlaceholderText" ikke "PlacholderText"
        min_combobox.addItem("Alternativ 1")  # Merk: "Alternativ" ikke "Alternatvi"
        min_combobox.addItem("Alternativ 2")
        layout.addWidget(min_combobox, 1, 2)

        # Tekstfelt
        min_text = QTextEdit()
        min_text.setPlaceholderText("Bruker input flere linjer")  # Merk: "PlaceholderText" ikke "PlacholderText"
        layout.addWidget(min_text, 2, 2)

        # Slider
        min_slider = QSlider()
        min_slider.setRange(10, 80)
        layout.addWidget(min_slider, 2, 1)

        # Vis beskjed ved knappetrykk
        min_knapp.clicked.connect(self.vis_beskjed)

        self.show()

    def vis_beskjed(self):
        min_beskjed = QMessageBox()
        min_beskjed.setText("Hei bruker, dette er en beskjed til deg")
        min_beskjed.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    vindu = Hovedvindu()
    sys.exit(app.exec())
