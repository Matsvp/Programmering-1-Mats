from car_dealership import Car

def rent_car_monthly_price(car):
    return car.rent_car_monthly_price()

# Test
car1 = Car("Toyota", "Corolla", 96000, 2012, 8, False, 163000)
print(f"Monthly Rent Price: {rent_car_monthly_price(car1)},-")
