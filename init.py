class Car:
    def __init__(self, brand, year=2024):
        self.brand = brand
        self.year = year

c1 = Car("Toyota")
print(c1.year)
