from webshop import add_number_or_ware_to_shopping_cart

# Eksempeldata
all_wares = {
    "amd_processor": {
        "name": "AMD Ryzen 9 5900X Processor",
        "price": 5590.0,
        "number_in_stock": 10,
        "ratings": [4.5, 4.0, 5.0],
        "description": "High-performance processor.",
    },
    "playstation_5": {
        "name": "PlayStation 5",
        "price": 5999.0,
        "number_in_stock": 0,
        "ratings": [5.0, 4.5, 4.0],
        "description": "Next-gen console.",
    },
}

# Handlekurv
shopping_cart = {}

# Legg til varer i handlekurven
add_number_or_ware_to_shopping_cart("amd_processor", all_wares["amd_processor"], shopping_cart, 5)
add_number_or_ware_to_shopping_cart("amd_processor", all_wares["amd_processor"], shopping_cart, 10)
add_number_or_ware_to_shopping_cart("playstation_5", all_wares["playstation_5"], shopping_cart, 1)

# Skriv ut handlekurven
print("\nShopping Cart:")
for key, quantity in shopping_cart.items():
    print(f"{key}: {quantity}")

