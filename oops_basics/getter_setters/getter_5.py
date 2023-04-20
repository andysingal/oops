class Backpack:
    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, new_items):
        print("Calling the setter...")
        if isinstance(new_items, list) :
            self._items = new_items
        else:
            print("Please enter a valid items")

    @items.deleter
    def items(self):
        del self._items

my_backpack = Backpack()
my_backpack.items = ["Water Bottle", "Sleeping Bag"]
print(my_backpack.items)