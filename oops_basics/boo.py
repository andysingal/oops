class Backpack:
    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items

    def add_item(self,item):
        self._items.append(item)

    def remove_item(self,item):
        if item in self._items:
            self._items.remove(item)
        else:
            print("This item is not in the backpack")

my_backpack = Backpack()

my_backpack.add_item("Water Bottle")
print(my_backpack.items)

