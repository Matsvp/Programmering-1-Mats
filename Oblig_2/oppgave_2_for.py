oddetall = [] # Lager en tom liste for å lagre oddetall
# For-løkke som går gjennom tall fra 9 til 101 (102 er eksklusiv, så det stopper ved 101)
for tall in range(9, 102):
    # Sjekker om tallet er et oddetall ved å se om resten ved deling på 2 ikke er lik 0
    if tall % 2 !=0:
        oddetall.append(tall) # Legger til oddetallet i listen 'oddetall'
# Skriver ut en melding til brukeren før listen
print('Her kommer en liste med alle oddetallene fra 9-101 i en liste')
# Skriver ut listen med alle oddetallene
print(oddetall)