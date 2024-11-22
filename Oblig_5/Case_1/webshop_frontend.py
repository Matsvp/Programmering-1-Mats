from webshop import (
    print_ware_information,
    calculate_average_ware_rating,
    get_all_wares_in_stock,
    add_number_or_ware_to_shopping_cart,
    calculate_shopping_cart_price
)
from wallet import Wallet

# Vareregister
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

# Demonstrasjon av funksjoner
print("Available products:")
wares_in_stock = get_all_wares_in_stock(all_wares)
for ware in wares_in_stock.values():
    print_ware_information(ware)

print("\nShopping Scenario:")
shopping_cart = {}
wallet = Wallet(10000)

add_number_or_ware_to_shopping_cart("amd_processor", all_wares["amd_processor"], shopping_cart, 2)
total_price = calculate_shopping_cart_price(shopping_cart, all_wares)
print(f"Total price (with tax): {total_price}")

# Sjekk om nok penger i lommeboka
if wallet.get_amount() >= total_price:
    wallet.subtract_amount(total_price)
    print(f"Purchase successful! Remaining balance: {wallet.get_amount()}")
else:
    print("Not enough money in the wallet to complete the purchase.")

