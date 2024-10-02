brettspill = {
    'tittel': 'Dixit', 
    'spilltid':30, 
    'aldersgrense':0
}

for key in brettspill.keys():
    print(key)

for value in brettspill.values():
    print(value)

for key, value in brettspill.items():
    print(f'{key} - {value}')