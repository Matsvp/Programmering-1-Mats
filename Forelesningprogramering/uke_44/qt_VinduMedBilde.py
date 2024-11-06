import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QPixmap

class Vindu(QWidget):
    def __init__(self):
        super().__init__()
        
        # Rettet skrivefeil i setWindowTitle
        self.setWindowTitle("Enkelt vindu")
        self.resize(300, 300)

        # Tekstlabel
        label = QLabel("Hello World")

        # Bilde-label
        label_img = QLabel()
        pixmap = QPixmap("pony.jpg")
        label_img.setPixmap(pixmap)

        # Layout
        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(label)
        layout.addWidget(label_img)

app = QApplication(sys.argv)
vindu = Vindu()
vindu.show()

sys.exit(app.exec())
