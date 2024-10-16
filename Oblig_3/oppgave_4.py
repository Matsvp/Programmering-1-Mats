def skriv_header():
    print('\n ========================================')
    print('== Hva er volumet av en kube? ==')
    print('==========================================')

def volum_kube(lengde, bredde, hoyde):
    volum = lengde * bredde * hoyde
    print(f'Volumet av kuben er {volum} cm^3')
    return volum

run = True
while run == True:
    skriv_header()

    hoyde = int(input("Skriv inn høyde i cm: "))
    lengde = int(input("Skriv inn lengde i cm: "))
    bredde = int(input("Skriv inn bredde i cm: "))

    if hoyde == 0 or lengde == 0 or bredde == 0:
        print('Du kan ikke ha en av sidene til en kube som er 0')
    elif hoyde < 0 or lengde < 0 or bredde < 0:
        print('Du kan ikke ha en av sidene til en kube som er negativ')
    else:
        volum_kube(lengde, bredde, hoyde)

    # Spør bruker om han/hun vil kjøre på nytt
    svar = input("Vil du kjøre programmet på nytt? (ja/nei): ").lower()
    if svar != 'ja':
        run = False
