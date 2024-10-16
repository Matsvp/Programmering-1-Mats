
def get_filmer():
    filmer = [
        {"tittel": "Inception", "år": 2010, "rating": 8.7},
        {"tittel": "Inside Out", "år": 2015, "rating": 8.1},
        {"tittel": "Con Air", "år": 1997, "rating": 6.9},
        {"tittel": "Forrest Gump", "år": 1994, "rating": 8.8},
        {"tittel": "The Dark Knight", "år": 2008, "rating": 9.0},
        {"tittel": "Starwars - Stjernekrigen", "år": 1977, "rating": 8.6}
    ]
    return filmer

filmer = get_filmer()
for film in filmer:
    print(f"{film['tittel']} - {film['år']} has a rating of {film['rating']}")

#Lager en funskjon som tar en liste med filmer som parameter og regner ut gjennomsnittsratingen for alle filmene i lista og returnerer dette
def gjennomsnittsrating(filmer):
    total_rating = 0
    for film in filmer:
        total_rating += film['rating']
    return total_rating / len(filmer)
gjennomsnittsrating_alle_filmer = gjennomsnittsrating(filmer)
print(f"Gjennomsnittsratingen for alle filmene er {gjennomsnittsrating_alle_filmer}") 

