from car_dealership import Car

def calculate_total_price(car):
    return car.calculate_total_price()

# Test
car1 = Car("Toyota", "Corolla", 96000, 2012, 8, False, 163000)
print(f"Total Price: {calculate_total_price(car1)},-")
