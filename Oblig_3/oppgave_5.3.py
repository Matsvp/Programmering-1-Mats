# Funksjon som returnerer listen med alle filmer
# Funksjon A: Skriv filmer til en fil
def skriv_filmer_til_fil(filmer_liste, filnavn):
    with open(filnavn, 'w') as fil:
        for film in filmer_liste:
            fil.write(f"{film['tittel']} - {film['aar']} has a rating of {film['rating']}\n")
    print(f"Filmer er skrevet til filen '{filnavn}'")

# Funksjon B: Les fra fil og skriv ut til terminalen
def les_fil_og_skriv_ut(filnavn):
    try:
        with open(filnavn, 'r') as fil:
            innhold = fil.read()
            print("Innholdet i filen er:\n")
            print(innhold)
    except FileNotFoundError:
        print(f"Filen '{filnavn}' finnes ikke.")

# Eksempel på bruk av funksjonene
filmer = [
        {"tittel": "Inception", "aar": 2010, "rating": 8.7},
        {"tittel": "Inside Out", "aar": 2015, "rating": 8.1},
        {"tittel": "Con Air", "aar": 1997, "rating": 6.9},
        {"tittel": "Forrest Gump", "aar": 1994, "rating": 8.8},
        {"tittel": "The Dark Knight", "aar": 2008, "rating": 9.0},
        {"tittel": "Starwars - Stjernekrigen", "aar": 1977, "rating": 8.6}
]

# Skrive filmer til en fil
skriv_filmer_til_fil(filmer, "movies.txt")

# Lese fra filen og skrive ut til terminalen
les_fil_og_skriv_ut("movies.txt")