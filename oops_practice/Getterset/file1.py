class Customer:
    def __init__(self,name, balance):
        self._name = name
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self,balance):
        if balance < 0:
            self.__balance = 0
        elif balance > 10000:
            self.__balance = 10000
        else:
            self.__balance = balance


    # def get_balance(self):
    #     return self.__balance
    #
    # def set_balance(self, balance):
    #     if balance < 0:
    #         self.__balance = 0
    #     elif balance > 10000:
    #         self.__balance = 10000
    #     else:
    #         self.__balance = balance


customer1 = Customer("Ankush", 10)
customer2 = Customer("Renad", 100)
customer1.balance = 100
print(customer1.balance)
