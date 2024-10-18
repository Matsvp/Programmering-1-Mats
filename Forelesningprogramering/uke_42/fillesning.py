
with open("Forelesningprogramering/uke_42/zen_of_phyton.txt") as fil:
    innhold = fil.read()
    print(innhold)
    print(type(innhold))

with open("Forelesningprogramering/uke_42/zen_of_phyton.txt") as fil:
    linjeliste = fil.readlines()
    print(linjeliste)
    print(type(linjeliste))

with open("Forelesningprogramering/uke_42/zen_of_phyton.txt") as fil:
    print(f'/n{fil.readline()} - første linje')
    print(f'{fil.readline()} - andre linje')
    print(f'{fil.readline()} - tredje linje')


filnavn = "Forelesningprogramering/uke_42/zen_of_phyton.txt"

try:
    with open(filnavn) as fil:
        print(fil.read())
except FileNotFoundError:
    print(f'Filen {filnavn} finnes ikke')