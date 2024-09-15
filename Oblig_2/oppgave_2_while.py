# Lager en tom liste som vi skal fylle med oddetall
oddetall = []
# Setter starttallet til 9
tall = 9
# Starter en løkke som kjører så lenge 'tall' er mindre enn eller lik 101
while tall <= 101:
     # Sjekker om tallet er et oddetall
    if tall % 2 != 0:
         # Hvis tallet er et oddetall, legg det til i 'oddetall'-listen
        oddetall.append(tall)
    # Øker tallet med 1 for å gå til neste tall
    tall += 1
# Skriver ut en melding og deretter listen med alle oddetallene fra 9 til 101
print('Her kommer en liste med alle oddetallene fra 9-101 i en liste')
print(oddetall)