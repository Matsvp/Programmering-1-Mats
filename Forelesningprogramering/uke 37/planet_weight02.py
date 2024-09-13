planeter = ["Merkus", "Venu", "Jorden", "Mars", "Jupiter", "Saturn", "Uranus", "Neptun"]
tyngdekraft = [3.7, 8.87, 9.807, 3.721, 24.79, 10.44, 8.87, 11.15]

print("----- Planeter -----")
print("1 - Merkur")
print("2 - Venus")
print("3 - Jorden")
print("4 - Mars")
print("5 - Jupiter")
print("6 - Saturn")
print("7 - Saturn")
print("8 - Neptun")

planetnummer = int(input("Velg et planetnummer"))
if (planetnummer <= 0 or planetnummer > len(planeter)):
    print("Du har valgt et for høyt eller for lavt tall")
    exit()

planetnummer = planetnummer - 1

print(f'Du har valgt planeten {planeter[planetnummer]}')

din_vekt = input("Hva er din vekt på Jorden? (i hele kg)")
din_vekt = int(din_vekt)

din_masse = din_vekt / tyngdekraft[2]
vekt_paa_planet = din_masse * tyngdekraft[planetnummer]

print(f'Din vekt på {planeter[planetnummer]} er {round(vekt_paa_planet, 2)}')