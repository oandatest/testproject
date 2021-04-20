
# OOP

class Product:
    def __init__(self, name, price, currency):
        self._name = name
        self._price = price
        self._currency = currency

    def get_info(self):
        s = f"Name: {self._name}, price:{self._price}, currency: {self._currency}"
        return s

    def __str__(self):
        return self.get_info()


# creating object based on class definition
product1 = Product("HDD 1TB", 299, "USD")
product2 = Product("TV SET", 1234, "EUR")
print(product1.get_info())
print(product2.get_info())
print(product1)
s = "ABCDEFGHIJ"
print(s)
