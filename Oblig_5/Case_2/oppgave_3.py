from car_dealership import Car

def get_car_age(car):
    return car.get_car_age()

# Test
car1 = Car("Toyota", "Corolla", 96000, 2012, 8, False, 163000)
print(f"Car Age: {get_car_age(car1)} years")
