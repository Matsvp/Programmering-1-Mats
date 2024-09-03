#Lager fem variabker for hver person og hvor mange småkaker de forskjellige har spist
person_1=5
person_2=9
person_3=2.5
person_4=21
person_5=0

#Lager en ny variabel på antall småkaker som er spist til sammen
antall_smaakaker=(person_1 + person_2 + person_3 + person_4 + person_5)
#Lager enda en variabel på antall personer som har spsit
antall_personer=5
#Ber den printe antall personer som har spist, og antall småkaker som har blidt spist
print("Antall småkaker som har blidt spist", antall_smaakaker)
print("Antall peroner", antall_personer)
#Lager en ny variabel som regner ut gjenomsittet på antall småkaker spist
gjennomsitt=int(antall_smaakaker/antall_personer)
#printer Gjennomsittet
print("Gjenomsittet av kaker som har blidt spist", gjennomsitt)