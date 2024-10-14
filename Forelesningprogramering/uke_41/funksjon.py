import random

def funksjon():
    #logikk
    return




def skriv_hei():
    print('-----------------')
    print('-------Hei-------')
    print('-----------------')
    return

skriv_hei()
skriv_hei()


def gi_et_tilfeldig_tall(startverdi, stoppverdi):
    tilfeldig_tall = random.randrange(startverdi, stoppverdi)
    return tilfeldig_tall

nytt_tall = gi_et_tilfeldig_tall(30,100)
print(nytt_tall)