class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def total(self, quantity):
        return self.price * quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if price < 0:   
            raise ValueError("Price cannot be negative.")
        self._price = price

try:

    product = Product("Notebook", 25)
    product.price = 30
    print(product.total(3))


    product.price = -1
except ValueError:
    print("Rejected")

