brettspill = {
    'tittel': 'Dixit', 
    'spilltid':30, 
    'aldersgrense':0
}

print(brettspill)
print()
print(brettspill['spilltid'])
print(f'Spilletiden er {brettspill["spilltid"]} minutter.')

brettspill['spilltid'] = 40
print(brettspill)

print(brettspill.get('spilltid'))

brettspill['beskrivelse'] = "Give the perfect clue so most (not all) players guess the right surreal image card"
print(brettspill)

brettspill.pop('beskrivelse')
print(brettspill)

del brettspill ['spilltid']
print(brettspill)