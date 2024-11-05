import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton


class Hovedvindu(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 500, 200, 100)

        self.setWindowTitle("QVBoxLayout-test")
        layout = QVBoxLayout()
        self.setLayout(layout)

        button1 = QPushButton('Knapp 1')
        button2 = QPushButton()
        button2.setText('Knapp 2')
        button3 = QPushButton("Knapp 3")

        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)

        self.show()

if __name__--'__main__':
    app = QApplication(sys.argv)
    vindu = Hovedvindu()

    sys.exit(app.exec())