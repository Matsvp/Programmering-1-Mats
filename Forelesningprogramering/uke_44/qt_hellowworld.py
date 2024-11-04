
import sys
from PyQt6.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)

vindu = QWidget()

vindu.setWindowTitle("Hello world")
vindu.resize(300,100)

vindu.show()