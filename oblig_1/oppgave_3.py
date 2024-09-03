#Printer ut en setning som forklarer hva programet gjør
print("Dette er en kalkulatort som ganger, deler, plusser, minuser, modulo, opphøyer, deler med nedruning")
#Ber brukeren å skrive inn et tall gjennom input som blir konvertert til desimal tall og blir den første variabelen
tall_1=float(input("Skriv inn det første tallet du vil ha i kalkulatoren"))
#Ber brukeren å skrive inn et tall gjennom input som blir konvertert til desimaltall og blir den andre variabelen
tall_2=float(input("Skriv inn det andre tallet du vil ha i kalkulatoren"))

#Her utfører den de forskjelige utregningende og gjør de om til nye variabler
#Eks "Gange" blir det førte tallet brukern la inn ganger det andre tallet
Gange=(tall_1*tall_2)
Dele=(tall_1/tall_2)
Pluss=(tall_1+tall_2)
Minus=(tall_1-tall_2)
Modulo=(tall_1 % tall_2)
Opphøde=(tall_1**tall_2)
Dele_med_nedrunding=(tall_1//tall_2)

#Her printer den ut alle de nye resultatene av de forskjelige mattestykkene
print("Gange:",Gange)
print("Dele:", Dele)
print("pluss:", Pluss)
print("Minus:", Minus)
print("Modulo:", Modulo)
print("Opphøde:", Opphøde)
print("Dele med nedrunding:",Dele_med_nedrunding)