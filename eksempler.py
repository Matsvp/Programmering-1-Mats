
try:
    resultat = 100 / 0
except ZeroDivisionError:
    print("Kan ikke dele med null.")



class Hund:
    def __init__(self, navn, alder):
        self.navn = navn
        self.alder = alder

    def bjeff(self):
        print(f"{self.navn} sier voff!")

# Opprette et hundeobjekt
min_hund = Hund("Max", 5)

# Bruke hundeobjektets metode
min_hund.bjeff()
