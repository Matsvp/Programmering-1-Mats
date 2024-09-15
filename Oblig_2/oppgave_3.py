# Oppretter en liste med forskjellige boktitler
books = ["The Hobbit", "Farmer Giles of Ham", "The Fellowship of the Ring", "The Two Towers", "The Return of the King", "The Adventures of Tom Bombadil", "Tree and Leaf"]
# Lager en ny liste 'selectet_books' som velger ut spesifikke bøker fra 'books'-listen

selectet_books = [books[b] for b in [0, 1, 5, 6]]
print(selectet_books)

# Legger til to nye bøker til 'books'-listen ved hjelp av 'extend()' metoden
books.extend(["The Silmarillion", "Unfinished Tales"])
print(books)
# Går gjennom hele 'books'-listen for å sjekke hver bok
for i in range(len(books)):
    # Sjekker om boken er en av de tre i "The Lord of the Rings"-serien
    if books[i] in ["The Fellowship of the Ring", "The Two Towers", "The Return of the King"]:
        # Hvis ja, legg til "The Lord of the Rings: " foran boktittelen
        books[i] = "The Lord of the Rings: " + books[i]

print(books)
