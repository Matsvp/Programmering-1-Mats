from webshop import calculate_average_ware_rating

# Eksempeldata for vare
wares = [
    {
        "name": "Example Ware",
        "price": 3999,
        "number_in_stock": 30,
        "ratings": [4.5, 4.0, 5.0, 3.5],
        "description": "A non-existent ware used only for this example."
    },
    {
        "name": "Empty Ratings Ware",
        "price": 2000,
        "number_in_stock": 10,
        "ratings": [],
        "description": "A ware with no ratings."
    }
]

for ware in wares:
    try:
        average_rating = calculate_average_ware_rating(ware)
        print(f"Average rating for '{ware['name']}': {average_rating}")
    except ZeroDivisionError:
        print(f"'{ware['name']}' has no ratings.")
