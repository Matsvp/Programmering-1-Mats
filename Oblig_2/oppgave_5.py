from random import randrange

# Funksjon for å simulere dartspill for én spiller
def dartspill_en_spiller():
    total_score = 0  # Initialiserer total score for spilleren
    for i in range(3):  # Spilleren kaster 3 piler
        score = randrange(0, 61)  # Genererer en tilfeldig score mellom 0 og 60
        print(f'Kast {i + 1}: {score} poeng')  # Skriver ut poeng for hvert kast
        total_score += score  # Legger til poengene fra kastet til totalscoren
    print(f'Total score: {total_score} poeng')  # Skriver ut totalpoengene for spilleren

# Kjør funksjonen for én spiller
dartspill_en_spiller()

# Funksjon for å simulere dartspill for flere spillere
def dartspill_flere_spillere():
    antall_spillere = int(input("Hvor mange skal spille? "))  # Tar inn antall spillere fra brukeren

    total_scores = []  # Liste for å lagre total score for hver spiller
    
    # Gå gjennom hver spiller
    for spiller_nummer in range(1, antall_spillere + 1):
        print(f'Spiller {spiller_nummer} sin tur:')
        total_score_more = 0  # Initialiserer total score for nåværende spiller

        # Hver spiller kaster 3 piler
        for i in range(3):
            score = randrange(0, 61)  # Genererer en tilfeldig score mellom 0 og 60
            print(f'Kast {i + 1}: {score} poeng')  # Skriver ut poeng for hvert kast
            total_score_more += score  # Legger til poengene fra kastet til spillerens totalscore

        # Legger til spillerens total score til listen over alle scorer
        total_scores.append(total_score_more)
        
    # Skriver ut totalscoren for alle spillere etter at alle har kastet
    print("Totale scorer for alle spillere:")
    for spiller_nummer in range(1, antall_spillere + 1):
        print(f'Spiller {spiller_nummer}: {total_scores[spiller_nummer - 1]} poeng')        

# Kjør funksjonen for flere spillere
dartspill_flere_spillere()