from datetime import date


#Begrunnelse for Tilleggsfunksjoner
#sell_car:

#Salg av bil er en logisk handling som hører hjemme i klassen, fordi salget handler om å endre eller fjerne bilens status (f.eks. fra registeret).
#update_kilometers:

#Kilometerstand er en dynamisk verdi som kan endres over tid. Denne metoden gjør det mulig å holde informasjonen oppdatert i bilens objekt.
#calculate_insurance_cost:

#Forsikringskostnader er avhengig av bilens egenskaper som pris, alder, og kilometerstand. Dette gjør det naturlig å plassere logikken i bilklassen.

class Car:
    def __init__(self, brand, model, price, year, month, is_new, km):
        self.brand = brand
        self.model = model
        self.price = price
        self.year = year
        self.month = month
        self.is_new = is_new
        self.km = km

    def print_car_information(self):
        """
        Skriver ut informasjon om bilen.
        """
        pass  # Implementasjon her

    def get_car_age(self):
        """
        Beregner bilens alder.
        """
        pass  # Implementasjon her

    def rent_car_monthly_price(self):
        """
        Beregner månedsleieprisen for bilen.
        """
        pass  # Implementasjon her

    def next_eu_control(self):
        """
        Beregner datoen for neste EU-kontroll.
        """
        pass  # Implementasjon her

    def calculate_total_price(self):
        """
        Beregner totalprisen for bilen inkludert avgifter.
        """
        pass  # Implementasjon her

    # Tilleggsfunksjoner fra del 3:
    def sell_car(self):
        """
        Håndterer salget av bilen.
        """
        pass  # Implementasjon her

    def update_kilometers(self, additional_km):
        """
        Oppdaterer bilens kilometerstand med nye kilometer.
        
        Parametere:
        additional_km - Antall nye kilometer som skal legges til.
        """
        pass  # Implementasjon her

    def calculate_insurance_cost(self):
        """
        Beregner kostnadene for forsikring basert på bilens egenskaper.
        """
        pass  # Implementasjon her
