from datetime import date

class Car:
    def __init__(self, brand, model, price, year, month, is_new, km):
        self.brand = brand
        self.model = model
        self.price = price
        self.year = year
        self.month = month
        self.is_new = is_new
        self.km = km

    def print_car_information(self):
        condition = "New" if self.is_new else "Used"
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: {self.price},-")
        print(f"Manufactured: {self.year}-{self.month}")
        print(f"Condition: {condition}")

    def get_car_age(self):
        current_year = date.today().year
        return current_year - self.year

    def rent_car_monthly_price(self):
        annual_rent = self.price * 0.40
        monthly_rent = annual_rent / 12
        if self.is_new:
            monthly_rent += 1000
        return round(monthly_rent, 2)

    def next_eu_control(self):
        production_date = date(self.year, self.month, 1)
        today = date.today()
        years_since_production = today.year - production_date.year
        periods_since_production = years_since_production // 2
        next_control_year = production_date.year + (periods_since_production + 1) * 2
        return date(next_control_year, self.month, 1)

    def calculate_total_price(self):
        age = self.get_car_age()
        if self.is_new:
            fee = 10783
        else:
            fee_table = [
                (0, 3, 6681),
                (4, 11, 4034),
                (12, 29, 1729),
                (30, float('inf'), 0)
            ]
            fee = 0
            for min_age, max_age, fee_amount in fee_table:
                if min_age <= age <= max_age:
                    fee = fee_amount
                    break
        return self.price + fee
