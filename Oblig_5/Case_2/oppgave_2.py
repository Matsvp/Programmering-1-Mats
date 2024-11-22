def create_car(car_register, brand, model, price, year, month, is_new, km):
    car = {
        "brand": brand,
        "model": model,
        "price": price,
        "year": year,
        "month": month,
        "new": is_new,
        "km": km
    }
    car_key = f"{brand.lower()}_{model.lower()}_{len(car_register)}"
    car_register[car_key] = car
    return car

# Test
car_register = {}
new_car = create_car(car_register, "Toyota", "Corolla", 96000, 2012, 8, False, 163000)
print(new_car)
