
import sys
from PyQt6.QtWidgets import QApplication, QWidget

# Opprett applikasjonsobjektet
app = QApplication(sys.argv)

# Opprett hovedvinduet
vindu = QWidget()
vindu.setWindowTitle("Hello World")
vindu.resize(300, 100)

# Vis vinduet
vindu.show()

# Kjør applikasjonens hovedløkke
sys.exit(app.exec())
