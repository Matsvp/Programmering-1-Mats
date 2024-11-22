from webshop import get_all_wares_in_stock

# Eksempel på vareregister
all_wares = {
    "amd_processor": {
        "name": "AMD Ryzen 9 5900X Processor",
        "price": 5590.0,
        "number_in_stock": 50,
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
    "hdmi_cable": {
        "name": "Belkin Ultra High Speed HDMI Cable - 2m",
        "price": 349.0,
        "number_in_stock": 3,
        "ratings": [5.0, 5.0, 4.5, 5.0],
        "description": "A high-speed overpriced HDMI cable.",
    }
}

# Få varer på lager
wares_in_stock = get_all_wares_in_stock(all_wares)

# Skriv ut informasjon om varer som er på lager
print("Wares in stock:")
for key, ware in wares_in_stock.items():
    print(f"{ware['name']} - {ware['number_in_stock']} in stock")


