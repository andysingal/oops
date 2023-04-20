class BouncyBall:

    def __init__(self, price, size, brand):
        self._price = price
        self._size = size
        self._brand = brand

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self._price = new_price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, new_size):
        if new_size in ["small", "medium", "large"]:
            self._size = new_size

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, new_brand):
        if isinstance(new_brand, str) and new_brand:
            self._brand = new_brand