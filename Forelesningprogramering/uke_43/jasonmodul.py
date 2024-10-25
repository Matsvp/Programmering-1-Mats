import json

def les_json(filnavn):
    try:
        with open(filnavn) as fil:
            data = json.load(fil)
            
    except FileNotFoundError:
        print(f'Filen {filnavn} finnes ikke')
    else:
        return data


def skriv_json(dictionary, filnavn):
    try:
        with open(filnavn, 'w') as fil:
            json.dump(dictionary, fil, indent=4)
    except FileNotFoundError:
        print(f'Filen {filnavn} finnes ikke')