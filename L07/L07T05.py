class Car:
    brand = ""
    model = ""
    price = ""
    def __str__(self):
        return self.brand + ", " + self.model +  ", " + str(self.price)
    def __init__(self, brand = "", model = "", price = 0):
        self.brand = brand
        self.model = model
        self.price = price
car1 = Car("Scoda", "Octavia", 3000)
car2 = Car("Audi", "A4", 4000)
car3 = Car("Volvo", "V70", 5000)
sum = car1.price + car2.price + car3.price
print("Auto:", car1)
print("Auto:", car2)
print("Auto:", car3)
print("Autojen hinta yhteensä:", sum)