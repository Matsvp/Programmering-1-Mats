#Legger inn variablene
a=6
b=3
c=2
#printer ut hva de forskjellige variablene er 
print("a =",a)
print("b =",b)
print("c =",c)
#Lager nye variabler gjennom matte stykkene som vi har fått i oppgaven
Stykke_a=(a + b * c)
Stykke_b=( (a + b) * c )
Stykke_c=(a / b / c )
Stykke_d=(a / (b / c) )
#printer ut svaret på de forskjellige stykkene, har også valgt å legge til selve stykket gjennom "" for at det skal bli lettere for brukeren
print("a + b * c =", Stykke_a)
print("(a + b) * c =", Stykke_b)
print("a / b / c =", Stykke_c)
print("a / (b / c) =",Stykke_d)
