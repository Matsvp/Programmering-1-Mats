# Oppretter en liste med bøker
books = ["The Hobbit", "Farmer Giles of Ham", "The Fellowship of the Ring", "The Two Towers", "The Return of the King", "The Adventures of Tom Bombadil", "Tree and Leaf"]
# Skriver ut den opprinnelige listen med alle bøker
print(books)

# Oppretter en tom liste for bøker i "The Lord of the Rings"-trilogien
lord_books = []
# Går gjennom hver bok i 'books'-listen
for book in books:
    # Sjekker om boken er en del av trilogien
    if book in ["The Fellowship of the Ring", "The Two Towers", "The Return of the King"]:
        # Hvis ja, legg til boken i 'lord_books'-listen
        lord_books.append(book)

# Skriv ut bøkene i "The Lord of the Rings" ved hjelp av to forskjellige metoder

# Metode 1: En enkel for-løkke som går gjennom listen direkte
print('Bøker i Lord of The Rings (metode 1):')
for book in lord_books:
    print(book)

# Metode 2: Bruke range() og indeks for å gå gjennom listen
print('Bøker i Lord of The Rings (metode 2):')
for i in range(len(lord_books)):
    print(lord_books[i])