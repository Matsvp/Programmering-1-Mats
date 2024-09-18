from random import choice  # Importerer choice fra random for å velge tilfeldige elementer fra en liste

# Funksjon for å simulere dartspill for flere spillere
def dartspill_flere_spillere():
    while True:  # Start en uendelig løkke
        # Tar inn antall spillere fra brukeren
        antall_spillere = int(input("Hvor mange skal spille? "))
        
        if antall_spillere == 0:
            print("Spillet trenger minimum en spiller. Prøv igjen.")
            continue  # Går tilbake til starten av løkken og spør på nytt
        
        # Tar inn antall piler og antall runder fra brukeren
        antall_piler = int(input("Hvor mange piler skal hver spiller kaste? "))
        antall_runder = int(input("Hvor mange runder skal de spille? "))
        
        break  # Hvis antall spillere er gyldig, bryt ut av løkken
    
    # Liste for å lagre total score for hver spiller
    total_scores = []  
    
    # Liste over gyldige poeng som kan oppnås i et kast
    gyldig_poeng = [0]  # Bom (0 poeng)
    gyldig_poeng += list(range(1, 21))  # Enkeltpoeng fra 1 til 20
    gyldig_poeng += [2 * i for i in range(1, 21)]  # Dobbel poeng fra 2 til 40
    gyldig_poeng += [3 * i for i in range(1, 21)]  # Trippel poeng fra 3 til 60
    gyldig_poeng += [25, 50]  # Outer bullseye (25 poeng) og inner bullseye (50 poeng)
    
    # Gå gjennom hver spiller
    for spiller_nummer in range(1, antall_spillere + 1):
        print(f'Spiller {spiller_nummer} sin tur:')
        total_score_more = 0  # Initialiserer total score for nåværende spiller
        
        # Løkke for antall runder
        for runder in range(antall_runder):
            print(f'Runde {runder + 1}:')
            
            # Hver spiller kaster et gitt antall piler per runde
            for i in range(antall_piler):
                # Velger en tilfeldig score fra listen over gyldige poeng
                score = choice(gyldig_poeng)  
                # Skriver ut poeng for hvert kast
                print(f'Kast {i + 1}: {score} poeng')  
                # Legger til poengene fra kastet til spillerens totalscore
                total_score_more += score  

        # Legger til spillerens total score til listen over alle scorer etter at alle runder er fullført
        total_scores.append(total_score_more)
        
    # Skriver ut totalscoren for alle spillere etter at alle har kastet
    print("Totale scorer for alle spillere:")
    for spiller_nummer in range(1, antall_spillere + 1):
        print(f'Spiller {spiller_nummer}: {total_scores[spiller_nummer - 1]} poeng')        

# Kjør funksjonen for flere spillere
dartspill_flere_spillere()