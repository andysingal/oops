class Backpack:
    def __init__(self):
        self.__items = ["Water Bottle", "First Aid"]

my_backpack = Backpack()
print(my_backpack._Backpack__items)

"""
An attribute is never really private in Python because even if you add a leading
underscore to the name of the attribute to follow the Python naming conventions or
if you add two leading underscores to trigger the process of name mangling, you can still
 access the value of the attribute directly, outside the class.

For example: for the BaseballBat class, the instance attributes weight and
 model are classified as “non-public”. weight is non-public by convention and model
is protected by the process of name mangling. However, they can still be accessed,
as illustrated in the interactive shell session below:

"""
"""
>>> class BaseballBat:

	def __init__(self, length, weight, model):
		self.length = length
		self._weight = weight
		self.__model = model

		
>>> baseball_bar = BaseballBat(42, 32, "MZM110")
>>> baseball_bar._weight
32
>>> baseball_bar._BaseballBat__model
'MZM110'
"""