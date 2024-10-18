import random

brettspill = ["Ubongo", "Pandemic", "Ludo", "Monopol", "Mysterium"]

def velg_tilfelgig_brettspill(spilliste):
    indexnummer = random.randrange(len(spilliste))
    return spilliste.pop(indexnummer)

valgt_brettspill = velg_tilfelgig_brettspill(brettspill[:])

print(f'Du valgte {valgt_brettspill}')
print(brettspill)