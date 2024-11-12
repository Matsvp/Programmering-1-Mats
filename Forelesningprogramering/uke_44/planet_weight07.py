import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel, QFormLayout, QComboBox, QDoubleSpinBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

planeter = ["Merkur", "Venus", "Jorden", "Mars", "Jupiter", "Saturn", "Uranus", "Neptun"]
tyngdekraft = [3.7, 8.87, 9.807, 3.721, 24.29, 10.44, 8.87, 11.15]

planetbilder = ['Forelesningprogramering/uke_44/bilder/sun.png', 'Forelesningprogramering/uke_44/bilder/merkur.png', 'Forelesningprogramering/uke_44/bilder/venus.jpg', 'Forelesningprogramering/uke_44/bilder/jorden.png',
                'Forelesningprogramering/uke_44/bilder/mars.png', 'Forelesningprogramering/uke_44/bilder/jupiter.png', 'Forelesningprogramering/uke_44/bilder/saturn.png',
                'Forelesningprogramering/uke_44/bilder/uranus.png', 'Forelesningprogramering/uke_44/bilder/neptun.png']

class Hovedvindu(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Planet vekt')
        self.setGeometry(100, 100, 500, 400)

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        # Topptekstlabel
        self.topplabel = QLabel()
        self.topplabel.setText('Hva er din vekt på andre planeter?')
        self.layout.addWidget(self.topplabel, 0, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignHCenter)

        # Skjema layout
        self.skjema = QFormLayout()

        # Meny for valg av planet
        self.meny_combobox = QComboBox()
        self.meny_combobox.setPlaceholderText('Velg en planet')
        self.meny_combobox.addItem('Tilfeldig planet')
        for planet in planeter:
            self.meny_combobox.addItem(planet)

        self.meny_combobox.activated.connect(self.oppdater_bilde)
        self.skjema.addRow(self.meny_combobox)

        # Input for vekt
        self.vekt_input = QDoubleSpinBox()
        self.vekt_input.setPrefix('Din vekt i kg:    ')
        self.vekt_input.setDecimals(1)
        self.skjema.addRow(self.vekt_input)

        # Knapp for å regne ut vekten
        self.regnutknapp = QPushButton('Regn ut')
        self.regnutknapp.clicked.connect(self.regn_ut)
        self.skjema.addRow(self.regnutknapp)

        self.layout.addLayout(self.skjema, 1, 0)

        # Label for bilde
        self.bildelabel = QLabel()
        self.pixmap = QPixmap(planetbilder[0])  # Standard bilde
        self.pixmap = self.pixmap.scaled(256, 256)
        self.bildelabel.setPixmap(self.pixmap)

        self.layout.addWidget(self.bildelabel, 1, 1)

        # Bunnlabel
        self.bunnlabel = QLabel('Velg en planet og skriv inn vekten din!')
        self.layout.addWidget(self.bunnlabel, 2, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.show()

    def oppdater_bilde(self):
        """Oppdater bildet basert på valgt planet i comboboxen."""
        valgt_index = self.meny_combobox.currentIndex()

        # Hvis "Tilfeldig planet" er valgt, bruk solbildet som standard (som er det første bildet i listen)
        if valgt_index == 0:
            self.pixmap = QPixmap(planetbilder[0])
        else:
            # Hent riktig bilde basert på valgt planet
            self.pixmap = QPixmap(planetbilder[valgt_index])

        # Skalere bildet og sette det på QLabel
        self.pixmap = self.pixmap.scaled(256, 256)
        self.bildelabel.setPixmap(self.pixmap)

    def regn_ut(self):
        """Beregner vekten på valgt planet eller tilfeldig planet."""
        planetnummer = self.meny_combobox.currentIndex()

        if planetnummer == 0:
            # Velg en tilfeldig planet hvis "Tilfeldig planet" er valgt
            planetnummer = random.randrange(1, len(planeter) + 1)
            ny_vekt = beregn_vekt(self.vekt_input.value(), tyngdekraft[planetnummer - 1])
            self.bunnlabel.setText(
                f'Du fikk planeten {planeter[planetnummer - 1]}. Din vekt på denne planeten med tyngdekraft {tyngdekraft[planetnummer - 1]} m/s² er {ny_vekt} kg.'
            )
            # Oppdater bildet for tilfeldig planet
            self.pixmap = QPixmap(planetbilder[planetnummer])
            self.pixmap = self.pixmap.scaled(256, 256)
            self.bildelabel.setPixmap(self.pixmap)
        else:
            # Beregn vekt på valgt planet
            ny_vekt = beregn_vekt(self.vekt_input.value(), tyngdekraft[planetnummer - 1])
            self.bunnlabel.setText(
                f'Du valgte planeten {planeter[planetnummer - 1]}. Din vekt på denne planeten med tyngdekraft {tyngdekraft[planetnummer - 1]} m/s² er {ny_vekt} kg.'
            )

def beregn_vekt(din_vekt, planettyngdekraft, jordtyngdekraft=9.807):
    """Beregner vekten på en annen planet basert på jordens tyngdekraft."""
    beregnet_vekt = (din_vekt / jordtyngdekraft) * planettyngdekraft
    return round(beregnet_vekt, 2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    vindu = Hovedvindu()
    sys.exit(app.exec())

