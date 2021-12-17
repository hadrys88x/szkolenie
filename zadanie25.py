class Product:

    def __init__(self, price, name, id):
        self.price = price
        self.name = name
        self.id = id

    def print_info(self):
        text = "nazwa: " + str(self.name) + ", cena:" + str(self.price) + ", id: " + str(self.id)
        print(text)

produkt = Product(5, "woda", 90)
produkt.print_info()