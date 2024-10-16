filmer = [{"tittel" : "Inception", "år" :  2010, "rating": 8.7 }, 
          {"tittel" : "Inside Out", "år" : 2015, "rating": 8.1 },
          {"tittel": "Con Air", "år" : 1997,  "rating": 6.9 },
          ]

print(filmer)

# Legger til tre filmer
filmer.extend([
    {"tittel" : "Forrest Gump" , "år" : 1994 , "rating" : 8.8},
    {"tittel" : "The Dark Knight" , "år" : 2008 , "rating" : 9.0},
    {"tittel" : "Starwars - Stjernekrigen" , "år" : 1977 , "rating" : 8.6}])

print(filmer)

# Gir filmen en default rating på 5.0 hvis det ikke gis noen rating som argument til funksjonen
def legg_til_film(tittel, år, rating=5.0):
    filmer.append({"tittel" : tittel, "år" : år, "rating" : rating})

# Eksempel på å legge til en film uten å spesifisere rating
legg_til_film("Alvin og Gjengen", 2007)
print(filmer)


