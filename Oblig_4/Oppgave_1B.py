class Filmer:

    def __init__(self,title,year,score):
        self.title = title
        self.year = year
        self.score = score

    def hent_info(self):
        return f"{self.title} ble utgitt i {self.year} og har en score på {self.score}"

film1 = Filmer("Inception", 2010, 8.8)
film2 = Filmer("The Martian", 2015, 8.0)
film3 = Filmer("Joker", 2019, 8.4)

print(film1.hent_info())
print(film2.hent_info())
print(film3.hent_info())