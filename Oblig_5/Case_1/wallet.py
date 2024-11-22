
class Wallet:
    def __init__(self, amount):
        self.amount = amount

    def get_amount(self):
        """
        Returnerer mengden penger i lommeboka.
        """
        return self.amount

    def subtract_amount(self, value):
        """
        Trekker et beløp fra lommeboka hvis det er nok penger.
        """
        if self.amount >= value:
            self.amount -= value
        else:
            raise ValueError("Not enough money in the wallet.")

