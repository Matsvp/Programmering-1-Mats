print("dette programet regner ut vekten din på andre planeter")

din_vekt = input('hva er din vekt på jorden? (i hele kg)')
if (din_vekt.isnumeric() == True):
    din_vekt = int(din_vekt)
    print("ok")
else:
    print(f'{din_vekt} er ikke en gyldig vekt (skriv heltall)')
    exit()

if (din_vekt <= 0):
    print(f'{din_vekt} er ikke positiv prøv igjen')
elif (din_vekt > 600):
    print(f'{din_vekt} er enten verdensrekord, eller så lyver du')
    exit()

planetnavn = input("hva er planetens navn")
if (planetnavn == "Pluto" or planetnavn == "pluto"):
    print("Pluto er ikke en planet")

planetens_tyngdekraft = input('Hva er planetens tyngdekraft')
planetens_tyngdekraft = float(planetens_tyngdekraft) 

if (planetens_tyngdekraft <= 0):
    print(f'Tyngdekraften, {planetens_tyngdekraft} kan ikke være lavere enn 0')
    exit()

jordens_tyngdekraft = 9.807

din_masse = din_vekt / jordens_tyngdekraft
din_planetvekt = din_masse * planetens_tyngdekraft
din_planetvekt = round(din_planetvekt, 2)

print(f'din vekt på planeten {planetnavn} med tyngdekraft {planetens_tyngdekraft} m/s2, er {din_planetvekt}kg')
