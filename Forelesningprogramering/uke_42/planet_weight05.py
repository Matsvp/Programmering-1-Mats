import random



def skriv_header():
    print('\n ========================================')
    print('== Hva er din vekt på en annnen planet? ==')
    print('==========================================')


def skriv_ut_planetliste(planeter_som_skal_skrives_ut):
    for index, planet in enumerate(planeter_som_skal_skrives_ut):
        print(f'{index} - {planet ['navn']}')

def velg_tilfeldig(valgt_samling):
    random_index = random.randrange(1, len(valgt_samling))
    valgt_element = valgt_samling[random_index]
    return valgt_element

def beregn_vekt(din_vekt, planettyngdekraft, jordtyngdekraft = 9.807):
    beregnet_vekt = (din_vekt / jordtyngdekraft) * planettyngdekraft
    return round(beregnet_vekt, 2)

def en_gang_til():
    svar = input('Vil du gjøre en ny beregning? (y/n): ')
    return svar.upper() == 'Y'


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

    if planetnummer == 0:
        valgt_planet = velg_tilfeldig(planeter)
        print(f'Du har fikk {valgt_planet["navn"]}')

    else:
        valgt_planet = planeter[planetnummer]
        print(f'Du har valgt {valgt_planet["navn"]}')
    #ta input med vekt
    brukervekt = float(input('Skriv inn din vekt: '))
    #beregninger
    vekt_pa_annen_planet = beregn_vekt(brukervekt, valgt_planet['tyngdekraft'])
    print(f'Din vekt på {valgt_planet["navn"]} med tyngdekraft er {valgt_planet['tyngdekraft']} er {vekt_pa_annen_planet} kg')
    #tilbakemeldinger
    
   

    #ta input om avslutning
    run = en_gang_til()
print('Takk for at du brukte programmet!')
    