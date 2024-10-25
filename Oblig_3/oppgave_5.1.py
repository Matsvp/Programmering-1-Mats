filmer = [{"tittel" : "Inception", "aar" :  2010, "rating": 8.7 }, 
          {"tittel" : "Inside Out", "aar" : 2015, "rating": 8.1 },
          {"tittel": "Con Air", "aar" : 1997,  "rating": 6.9 },
          ]

def skriv_ut_filmer(filmer):
    for film in filmer:
        print(f"Tittel: {film['tittel']}, aar: {film['aar']}, Rating: {film['rating']}")

skriv_ut_filmer(filmer)
print("\n")

# Legger til tre filmer
filmer.extend([
    {"tittel" : "Forrest Gump" , "aar" : 1994 , "rating" : 8.8},
    {"tittel" : "The Dark Knight" , "aar" : 2008 , "rating" : 9.0},
    {"tittel" : "Starwars - Stjernekrigen" , "aar" : 1977 , "rating" : 8.6}])

skriv_ut_filmer(filmer)
print("\n")

# Gir filmen en default rating på 5.0 hvis det ikke gis noen rating som argument til funksjonen
def legg_til_film(tittel, aar, rating=5.0):
    filmer.append({"tittel" : tittel, "aar" : aar, "rating" : rating})

# Eksempel på å legge til en film uten å spesifisere rating
legg_til_film("Alvin og Gjengen", 2007)
skriv_ut_filmer(filmer)


