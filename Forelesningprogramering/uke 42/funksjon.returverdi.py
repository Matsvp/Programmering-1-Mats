#import math
from math import log
def hundealder_til_menneskealder(hundealder):
    mennekealder = 16 * log(hundealder) + 31
    return mennekealder

print(hundealder_til_menneskealder(50))
menneske_alder = hundealder_til_menneskealder(10)
print(menneske_alder)

def inkuder_moms(pris, moms=0.25):
    pris_med_moms = pris + pris*moms
    return pris_med_moms


pris_uten_moms =100
print(inkuder_moms(pris_uten_moms))