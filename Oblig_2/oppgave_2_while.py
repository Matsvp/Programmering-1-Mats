oddetall = []

tall = 9
while tall <= 101:
    if tall % 2 != 0:
        oddetall.append(tall)
    tall += 1

print('her kommer en liste med alle oddetallene fra 9-101 i en liste')
print(oddetall)