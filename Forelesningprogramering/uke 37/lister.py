planeter = ['Merkur','Venus','Tellus','Jupiter','Saturn','Uranus']
print(planeter)

print(planeter[2])

planeter[3] = "Mars"
print(planeter)

planeter.append('Neptun')
print(planeter)
planeter.append('Pluto')
print(planeter)

planeter.insert(4,'Jupiter')
print(planeter)

planeter.pop()
print(planeter)

planeter.pop(3)
print(planeter)

planeter.append('Saturn')
print(planeter)

planeter.remove('Saturn')
print(planeter)

print('midlertidig sortert list:')
print(sorted(planeter))

planeter.reverse
print(planeter)

planeter.sort()
print(planeter)

planeter.sort(reverse=True)
print(planeter)


antall_planeter = len(planeter)
print(len(planeter))

#random_liste = ['Europa', 7,['Ny liste', 23, 'med nye elementer'],'Bil']

#print(random_liste[2])
#print(random_liste[2][1])
#random_liste[2][2] = 'Forelesning'
#print(random_liste)

#random_liste[2].insert(1, "spørsmål i timen")
#print(random_liste[2])