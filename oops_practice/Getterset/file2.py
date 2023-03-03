# class CookieJar:
#     def __init__(self, cookie_number):
#         self.cookie_number = cookie_number
#
#     @property
#     def cookie_number(self):
#         return self.__cookie_number
#
#     @cookie_number.setter
#     def cookie_number(self, cookie_number):
#         self.__cookie_number = cookie_number
#
# jar_cookie = CookieJar(5)
# print(jar_cookie.cookie_number)

class Person:
    def __init__(self,name):
        self._name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        self._name = value
print(Person.__dict__)