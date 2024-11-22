from webshop import is_number_of_ware_in_stock

# Eksempel på varer
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
}

# Lager sjekkeksempler
def check_stock(ware, number_of_ware):
    if is_number_of_ware_in_stock(ware, number_of_ware):
        print(f"There are at least {number_of_ware} of {ware['name']} in stock.")
    else:
        print(f"There are not enough {ware['name']} in stock for your request.")

# Demonstrasjon
check_stock(all_wares["amd_processor"], 10)  # 10 på lager
check_stock(all_wares["amd_processor"], 60)  # Ikke nok
check_stock(all_wares["playstation_5"], 1)   # Ingen på lager
