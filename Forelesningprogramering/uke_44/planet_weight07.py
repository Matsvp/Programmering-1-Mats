import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel, QFormLayout, QComboBox, QDoubleSpinBox, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QIcon

planeter = ["Merkur", "Venus", "Jorden", "Mars", "Jupiter", "Saturn", "Uranus", "Neptun"]
tyngdekraft = [3.7, 8.87, 9.807, 3.721, 24.29, 10.44, 8.87, 11.15]

class Hovedvindu(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Planet vekt')
        self.setGeometry(100, 100, 500, 400)

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.topplabel = QLabel()
        self.topplabel.setText('Hva er din vekt på andre planeter?')
        self.layout.addWidget(self.topplabel, 0, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    vindu = Hovedvindu()
    sys.exit(app.exec())
