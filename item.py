class Item:
    def __init__(self, name, price,category):
        if price<=0:
            raise ValueError("Price must be greater than 0")
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"{self.name} {self.price} {self.category}"

    def __repr__(self):
        return self.__str__()