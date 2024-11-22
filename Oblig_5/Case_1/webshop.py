

def print_ware_information(ware):
    """
    Skriver ut informasjon om en vare.
    """
    print(f"Name: {ware['name']}")
    print(f"Price: {ware['price']},-")
    print(f"Number in stock: {ware['number_in_stock']}")
    print(f"Description: {ware['description']}")


def calculate_average_ware_rating(ware):
    """
    Beregner den gjennomsnittlige ratingen for en vare.
    """
    ratings = ware.get("ratings", [])
    if not ratings:
        raise ZeroDivisionError("Rating-listen er tom.")
    return round(sum(ratings) / len(ratings), 1)


def get_all_wares_in_stock(all_wares):
    """
    Returnerer alle varer som er på lager.
    """
    return {key: ware for key, ware in all_wares.items() if ware["number_in_stock"] > 0}


def is_number_of_ware_in_stock(ware, number_of_ware):
    """
    Sjekker om et spesifisert antall av en vare er på lager.
    """
    return ware["number_in_stock"] >= number_of_ware


def add_number_or_ware_to_shopping_cart(ware_key, ware, shopping_cart, number_of_ware=1):
    """
    Legger til en vare med et gitt antall i en handlekurv.
    """
    available_stock = ware["number_in_stock"]
    if available_stock >= number_of_ware:
        shopping_cart[ware_key] = shopping_cart.get(ware_key, 0) + number_of_ware
        ware["number_in_stock"] -= number_of_ware
        print(f"Added {number_of_ware} of {ware['name']} to the shopping cart.")
    elif available_stock > 0:
        shopping_cart[ware_key] = shopping_cart.get(ware_key, 0) + available_stock
        ware["number_in_stock"] = 0
        print(f"Only {available_stock} of {ware['name']} were added to the shopping cart.")
    else:
        print(f"{ware['name']} is out of stock.")


def calculate_shopping_cart_price(shopping_cart, all_wares, tax=25.0):
    """
    Beregner prisen for en handlekurv inkludert skatt.
    """
    total_price = 0
    for ware_key, quantity in shopping_cart.items():
        ware = all_wares.get(ware_key)
        if ware:
            total_price += ware["price"] * quantity
    return round(total_price * (1 + tax / 100), 2)

