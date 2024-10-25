import jasonmodul

planet = {'navn': 'Merkur', 'tyngdekraft': 3.7}
file_name = 'planet.json'
string ='denne er en string'

jasonmodul.skriv_json(planet, file_name)

innhold_fra_fil = jasonmodul.les_json(file_name)
print(innhold_fra_fil)

print(innhold_fra_fil['navn'])