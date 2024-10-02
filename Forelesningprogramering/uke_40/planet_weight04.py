import random

planeter = ["Merkus", "Venus", "Jorden", "Mars", "Jupiter", "Saturn", "Uranus", "Neptun"]
tyngdekraft = [3.7, 8.87, 9.807, 3.721, 24.29, 10.44, 8.87, 11.15]

kjør = True
while kjør:
    print('\n ========================================')
    print('== Hva er din vekt på en annnen planet? ==')
    print('==========================================')

    #for planetnummer in range (len(planeter)):
        #print(f'{planetnummer + 1} - {planeter[planetnummer]}')

    for planetnummer, planet in enumerate(planeter):
        print(f'{planetnummer +1} - {planet}')
    print('0 - Tilfeldig planet')

    valgt_planetnummer = input('\n Velg en planet ved å skrive et tall:')
    valgt_planetnummer = int(valgt_planetnummer) -1

    if valgt_planetnummer == -1:
        valgt_planetnummer = random.randrange(0,8)
        valgt_planet = planeter[valgt_planetnummer]
        print(f'Du fikk planeten: {valgt_planet}')
    
    else:
        valgt_planet = planeter[valgt_planetnummer]
        print(f'Du har valgt planeten: {valgt_planet}')



    din_vekt = float(input('Hva er din vekt'))

    #utrenginger
    jordens_tyngdekraft = tyngdekraft[2]
    din_masse = din_vekt / jordens_tyngdekraft
    din_vekt_på_planet = round (din_masse * tyngdekraft[valgt_planetnummer], 2)

    print(f'Din vekt på planeten {valgt_planet} er {din_vekt_på_planet} KG, som har tyngdekraft {tyngdekraft[valgt_planetnummer]}')


    en_gang_til = input('vil du prøve igjen? Y/N')
    
    kjør = en_gang_til.upper() == 'Y'

print('Takk for at du spilte')