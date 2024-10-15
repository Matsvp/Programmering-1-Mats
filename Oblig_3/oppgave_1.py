#En dictionary med informasjon om en student
student = { 
    "first name" : "Ola", 
    "last name" : "Nordmann",
    "favourite course" : "Programmering 1" 
} 
#Skriv ut studentens fulle navn
print(f'Mitt fulle navn er {student["first name"]} {student["last name"]}')

#Endrer favorittkurs til å inkludere kursets emnekode: "ITF10219 Programmering 1"
student["favourite course"] = "ITF10219 Programmering 1"
print(f'Mitt fulle navn er {student["first name"]} {student["last name"]}, og mitt favorittkurs er {student["favourite course"]}')

#Legger til en alder for studenten i dictionarien.
student["age"] = 19
print(f'Mitt fulle navn er {student["first name"]} {student["last name"]}, og jeg er {student["age"]} år gammel. Mitt favorittkurs er {student["favourite course"]}')
