x=3
y=300

er_x_storre_enn_y = x > y

if (er_x_storre_enn_y == True):
    print(f'{x} er større enn {y}')
else:
    print(f'{x} er ikke større enn {y}')
#-----------

number = -10
if (number > 0):
    print(f'{number} er et positivt tall.')
elif (number < 0):
    print(f'{number} er et negativt tall.')
elif (number > 0):
    print("dette er test to for neggativt tall")
else:
    print(f'{number} er 0.')

#-----------
navn1 = "nils-christian"
navn2 = "Nils-CHRIstIan"

if (navn1.lower() == navn2.lower()):
    print("navnene er like")
else:
    print("Navnene er ikke like")

