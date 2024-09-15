# Start med en tom liste
liste = []

# Kjør en løkke som fortsetter til brukeren velger å stoppe
while True:
    # Tar inn kommandoen fra brukeren
    komando = input('Skriv "L" for å legge til ting, "T" for å fjerne ting, "H" for å vise hele listen, og "stopp" for å stoppe programmet.')

    # Sjekk hva brukeren vil gjøre
    if komando == "L" or "l": 
        # Hvis brukeren vil legge til noe, spør etter det
        ting = input("Hva vil du legge til? ")
        liste.append(ting)  # Legger til elementet i listen
        print(f'"{ting}" er lagt til i listen.')

    elif komando == "T" or "t":
        # Hvis brukeren vil fjerne noe, spør etter hva de vil fjerne
        ting = input("Hva vil du ta bort fra listen? ")
        if ting in liste:
            liste.remove(ting)  # Fjerner elementet fra listen hvis det finnes
            print(f'"{ting}" er fjernet fra listen.')
        else:
            # Hvis elementet ikke finnes i listen
            print(f'"{ting}" finnes ikke i listen.')

    elif komando == "H" or "h":
        # Hvis brukeren vil se hele listen
        print("Her er listen:")
        for H in liste:
            print(H)  # Skriver ut hvert element i listen

    elif komando.lower() == "stopp" or "Stopp":
        # Hvis brukeren vil stoppe programmet
        print("Programmet er ferdig.")
        print(f'Her er listen: {liste} i tilfelle du trenger det senere :)')
        break  # Avslutter løkken

    else:
        # Hvis brukeren skriver noe annet enn "L", "T", "H", eller "stopp"
        print('Ugyldig kommando. Vennligst skriv "L", "T", "H", eller "stopp".')
    
    print()  # Legger til en tom linje for å gjøre utdataene mer oversiktlige