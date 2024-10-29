from planet_functions import *
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
    