



def skriv_header():
    print('\n ========================================')
    print('== Hva er din vekt på en annnen planet? ==')
    print('==========================================')


def skriv_ut_planetliste(planeter_som_skal_skrives_ut):
    for index, planet in enumerate(planeter_som_skal_skrives_ut):
        print(f'{index} - {planet ['navn']}')


planeter = [{'navn' : 'Tilfeldig planet'},
            {'navn' : 'Merkur', 'tyngdekraft' : 3.7},
            {'navn' : 'Venus', 'tyngdekraft' : 8.87},
            {'navn' : 'Jorda', 'tyngdekraft' : 9.807},
            {'navn' : 'Mars', 'tyngdekraft' : 3.721},
            {'navn' : 'Jupiter', 'tyngdekraft' : 24.79},
            {'navn' : 'Saturn', 'tyngdekraft' : 10.44},
            {'navn' : 'Uranus', 'tyngdekraft' : 8.87},
            {'navn' : 'Neptun', 'tyngdekraft' : 11.15},
            ]

#---------------------------------------

run = True
while run == True:
    #"PSEUDOKODE"

    #Skriv ut overskrift
    skriv_header()


    #Skriv ut liste over planeter
    skriv_ut_planetliste(planeter)

    #ta input med valg, og en tilbakemelding
    planetnummer = int(input('\n Velg en planent ved å skrive inn et tall: '))
    #ta input med vekt
    #beregninger
    #tilbakemeldinger

    #ta input om avslutning

    #midlertigavslutningskode
    run = False