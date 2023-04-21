class Backpack:
    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items

    def add_item(self, item):
        if isinstance(item,str):
            self._items.append(item)
        else:
            print("Please provide a valid item")

    def remove_item(self,item):
        if item in self._items:
            self._items.remove(item)
            return 1
        else:
             return 0
    def has_items(self,item):
        return item in self._items

my_backpack = Backpack()
print(my_backpack.items)

my_backpack.add_item("Water Bottle")
print(my_backpack.items)


# class SchoolBus:
#
#     def __init__(self, color):
#         self._color = color
#
#     def welcome_student(self, student_name):
#         print(f"Hello {student_name}, how are you today?")