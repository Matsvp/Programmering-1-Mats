from random import choice

# Funksjon for å simulere dartspill for flere spillere
def dartspill_flere_spillere():
    while True:
        try:
            # Tar inn antall spillere fra brukeren
            antall_spillere = int(input("Hvor mange skal spille? "))
            
            if antall_spillere <= 0:
                print("Spillet trenger minimum én spiller. Prøv igjen.")
                continue  # Går tilbake til starten av løkken og spør på nytt
            
            break  # Hvis antall spillere er gyldig, bryt ut av løkken
        
        except ValueError:
            print("Ugyldig input, skriv inn et tall.")
            continue  # Går tilbake til starten og prøver igjen hvis brukeren skriver noe annet enn et tall

    # Liste for å lagre gjenstående poeng for hver spiller
    remaining_scores = [301 for _ in range(antall_spillere)] 

    # Liste for å sjekke om hver spiller har startet (må treffe dobbel for å starte)
    har_startet = [False for _ in range(antall_spillere)]
    
    # Liste over gyldige poeng som kan oppnås i et kast
    gyldig_poeng = [0]  # Bom (0 poeng)
    gyldig_poeng += list(range(1, 21))  # Enkeltpoeng fra 1 til 20
    gyldig_poeng += [2 * i for i in range(1, 21)]  # Dobbel poeng fra 2 til 40
    gyldig_poeng += [3 * i for i in range(1, 21)]  # Trippel poeng fra 3 til 60
    gyldig_poeng += [25, 50]  # Outer bullseye (25 poeng) og inner bullseye (50 poeng)
    
    # Prekalkulere listen over gyldige dobler
    gyldige_dobler = [2 * i for i in range(1, 21)]
    
    # Spill kontinuerlig til en vinner er funnet
    while True:
        # Gå gjennom hver spiller
        for spiller_nummer in range(antall_spillere):
            print(f'\nSpiller {spiller_nummer + 1} sin tur:')
            print(f"Spiller {spiller_nummer + 1} har {remaining_scores[spiller_nummer]} poeng igjen.")
            
            # Hver spiller får kaste tre piler per runde
            for i in range(3):
                score = choice(gyldig_poeng)  # Velg en tilfeldig score

                if not har_startet[spiller_nummer]:  # Hvis spilleren ikke har startet ennå
                    if score in gyldige_dobler:  # Treffer en dobbel
                        har_startet[spiller_nummer] = True
                        print(f'Kast {i + 1}: {score} poeng - Startet med dobbel!')
                    else:
                        print(f'Kast {i + 1}: {score} poeng - Må treffe dobbel for å starte.')

                else:
                    # Hvis spilleren har startet, sjekk om kastet holder seg over 0
                    if remaining_scores[spiller_nummer] - score < 0:
                        print(f'Kast {i + 1}: {score} poeng - Overstiger 0, kast ugyldig.')
                    else:
                        remaining_scores[spiller_nummer] -= score
                        print(f'Kast {i + 1}: {score} poeng, gjenstående: {remaining_scores[spiller_nummer]}')
                    
                    # Sjekk om spilleren har nådd nøyaktig 0
                    if remaining_scores[spiller_nummer] == 0:
                        print(f'\nSpiller {spiller_nummer + 1} vinner!')
                        return  # Avslutt spillet når en spiller vinner
# Kjør funksjonen for flere spillere
dartspill_flere_spillere()