class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name
        


class Honeybadger(Animal):
    def __init__(self, name, age, sgiven=0):
        super().__init__(name, age)
        self.sgiven = sgiven



dyr1 = Honeybadger ('Nils-Christian', 20, 2)
nils_nilsen = Animal('Nils Nilsen', 10)


print(dyr1.get_name())
print(dyr1.sgiven)
print(dyr1.age)