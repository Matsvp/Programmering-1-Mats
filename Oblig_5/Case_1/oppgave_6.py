from webshop import calculate_shopping_cart_price

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
shopping_cart = {
    "amd_processor": 2,  # 2 prosessorer
    "playstation_5": 1,  # 1 PlayStation
}

# Beregn prisen på handlekurven med skatt
total_price = calculate_shopping_cart_price(shopping_cart, all_wares)
print(f"Total price including tax: {total_price},-")

