# def my_decorator(fn):
#     print('decorating function')
#     def inner(*args, **kwargs):
#         print('running decorated function')
#         return fn(*args, **kwargs)
#     return inner
#
# @my_decorator
# def my_func(a, b):
#     print('running original function')
#     return a + b
#
# print(my_func(10,20))

class Person:
    def __init__(self,name):
        self._name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        self._name = value
"""
class Person:
    def __init__(self, name):
        self._name = name
        
    name = property()  # an "empty" prroperty - no getter or setter
    
    @name.setter
    def name(self, value):
        self._name = value
        
    @name.getter
    def name(self):
        return self._name
"""


p = Person('Guido')
print(p.name)