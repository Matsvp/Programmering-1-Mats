
my_earth_weight =input("Hvor mye veier du?")

my_earth_weight = float(my_earth_weight)

earth_gravety = 9.807
moon_gravety = 1.602

moon_weight = my_earth_weight / earth_gravety * moon_gravety

print(f' Din vekt på månen er {moon_weight}Kg!')