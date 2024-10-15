import random

brettspill = ["Ubongo", "Pandemic", "Ludo", "Monopol", "Mysterium"]

def velg_tildeldig_brettspill(Spilliste):
    indexnummer = random.randrange(len(Spilliste))
    return indexnummer
    