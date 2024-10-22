import json

planeter = [
            {'navn' : 'Merkur', 'tyngdekraft' : 3.7},
            {'navn' : 'Venus', 'tyngdekraft' : 8.87},
            {'navn' : 'Jorda', 'tyngdekraft' : 9.807}]

filnavn = 'planeter.json'

with open (filnavn, 'w') as utfil:
    json.dump(planeter, utfil, indent=4)

with open(filnavn, 'r') as fil:
    planeter_fra_fil = json.load(fil)
    print(planeter_fra_fil)
    print(type(planeter_fra_fil))



json_string = '{"dyr": "hund", "navn": "Disco", "alder": "5"}'
print(json_string)
print(type(json_string))

hund = json.loads(json_string)
print(hund)
print(type(hund))

print(f'Hunden heter {hund["navn"]} er en {hund["dyr"]} og er {hund["alder"]} år gammel')