#En dictionary med informasjon om en student
student = { 
    "first_name" : "Ola", 
    "last_name" : "Nordmann",
    "favourite_course" : "Programmering 1" 
} 
#Skriv ut studentens fulle navn
print(f'Mitt fulle navn er {student["first_name"]} {student["last_name"]}')

#Endrer favorittkurs til å inkludere kursets emnekode: "ITF10219 Programmering 1"
student["favourite course"] = "ITF10219 Programmering 1"
print(f'Mitt fulle navn er {student["first_name"]} {student["last_name"]}, og mitt favorittkurs er {student["favourite_course"]}')

#Legger til en alder for studenten i dictionarien.
student["age"] = 19
print(f'Mitt fulle navn er {student["first_name"]} {student["last_name"]}, og jeg er {student["age"]} år gammel. Mitt favorittkurs er {student["favourite course"]}')
