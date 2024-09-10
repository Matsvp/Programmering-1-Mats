# Tar input fra brukeren og konverterer det til et heltall (int)
ultimate_spørsmålet = int(input("Hva er svaret på det ultimate spørsmålet om livet, universet og alle ting? Hint: Det er et tall."))

 
# Sjekker om tallet er nøyaktig 42
if ultimate_spørsmålet == 42:
    # Hvis tallet er 42, skriv ut riktig melding
    print("Det stemmer, meningen med livet er 42!")

# Hvis tallet ikke er 42, sjekker om det er mellom 30 og 50
elif ultimate_spørsmålet > 30 and ultimate_spørsmålet < 50:
     # Hvis tallet er mellom 31 og 49, skriv ut "Nærme, men feil."
    print("Nærme, men feil.")
# Hvis tallet ikke er 42 og ikke mellom 31 og 49, skriv ut "FEIL!"
else:
    print("FEIL!")