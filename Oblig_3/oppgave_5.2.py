
def get_filmer():
    filmer = [
        {"tittel": "Inception", "aar": 2010, "rating": 8.7},
        {"tittel": "Inside Out", "aar": 2015, "rating": 8.1},
        {"tittel": "Con Air", "aar": 1997, "rating": 6.9},
        {"tittel": "Forrest Gump", "aar": 1994, "rating": 8.8},
        {"tittel": "The Dark Knight", "aar": 2008, "rating": 9.0},
        {"tittel": "Starwars - Stjernekrigen", "aar": 1977, "rating": 8.6}
    ]
    return filmer


def print_filmer(filmer):
    for film in filmer:
        print(f"{film['tittel']} - {film['aar']} has a rating of {film['rating']}")

filmer = get_filmer()
print_filmer(filmer)


#Lager en funskjon som tar en liste med filmer som parameter og regner ut gjennomsnittsratingen for alle filmene i lista og returnerer dette
def gjennomsnittsrating(filmer):
    total_rating = 0
    for film in filmer:
        total_rating += film['rating']
    return total_rating / len(filmer)
gjennomsnittsrating_alle_filmer = gjennomsnittsrating(filmer)
print(f"Gjennomsnittsratingen for alle filmene er {gjennomsnittsrating_alle_filmer}") 

def filmer_fra_og_med_aar(filmliste, aarstall):
    # Bruker list comprehension til å filtrere ut filmer fra og med det gitte året
    return [film for film in filmliste if film['aar'] >= aarstall]

# Henter listen over filmer
filmer = get_filmer()

# Bruker funksjonen til å finne alle filmer fra og med 2010
filmer_2010_og_senere = filmer_fra_og_med_aar(filmer, 2010)

# Printer ut informasjon om alle filmer fra og med 2010
print("\nFilmer fra og med 2010:")
for film in filmer_2010_og_senere:
    print(f"Tittel: {film['tittel']}, År: {film['aar']}, Rating: {film['rating']}")

