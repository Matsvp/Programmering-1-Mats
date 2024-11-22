from car_dealership import Car

def next_eu_control(car):
    return car.next_eu_control()

# Test
car1 = Car("Toyota", "Corolla", 96000, 2012, 8, False, 163000)
print(f"Next EU Control: {next_eu_control(car1)}")
