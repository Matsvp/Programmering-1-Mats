
class Filmer:

    def __init__(self,title,year,score):
        self.title = title
        self.year = year
        self.score = score



film1 = Filmer("Inception", 2010, 8.8)
film2 = Filmer("The Martian", 2015, 8.0)
film3 = Filmer("Joker", 2019, 8.4)

print(f"{film1.title} ble utgitt i {film1.year} og har en score på {film1.score}")
print(f"{film2.title} ble utgitt i {film2.year} og har en score på {film2.score}")
print(f"{film3.title} ble utgitt i {film3.year} og har en score på {film3.score}")
