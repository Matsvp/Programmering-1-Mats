from math import log


hoyde = int(input("Skriv inn høyde i cm: "))
lengde = int(input("Skriv inn lengde i cm: "))
bredde = int(input("Skriv inn bredde i cm: "))


def volum_kube(lengde, bredde, hoyde):
    volum = lengde * bredde * hoyde
    print(f'Volumet av kuben er {volum} cm^3')
    return volum

volum_kube(lengde, bredde, hoyde)
