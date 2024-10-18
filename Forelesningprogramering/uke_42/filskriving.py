
with open("Forelesningprogramering/uke_42/test.txt", 'w') as fil:
    while True:
        brukertekst = input('Skriv noe: ')

        if brukertekst == 'exit':
            break

        fil.write(brukertekst + '\n')
        