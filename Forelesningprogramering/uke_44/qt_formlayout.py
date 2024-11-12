import sys
from PyQt6.QtWidgets import QApplication, QWidget, QFormLayout, QPushButton, QLineEdit

class Hovedvindu(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Oppmeldingsskjema')
        self.setGeometry(100, 100, 300, 100)

        layout = QFormLayout()
        self.setLayout(layout)

        layout.addRow('Navn:', QLineEdit(self))
        layout.addRow('Epost:', QLineEdit(self))
        layout.addRow('Passord:', QLineEdit(self, echoMode=QLineEdit.EchoMode.Password))
        layout.addRow('Gjenta Passord:', QLineEdit(self, echoMode=QLineEdit.EchoMode.Password))
        layout.addRow(QPushButton('Meld meg opp'))

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    vindu = Hovedvindu()  # Merk parentesene for å opprette et objekt

    sys.exit(app.exec())

