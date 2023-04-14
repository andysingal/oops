from Timezone_class import TimeZone
import itertools
import numbers

class Account:
    transaction_counter = itertools.count(100)
    interest_rate = 0.5  # percentage

    def __init__(self, account_number,first_name,last_name, timezone=None,initial_balance=0):
        self._account_number = account_number
        self._first_name = first_name
        self.last_name = last_name

        if timezone is None:
            timezone = TimeZone('UTC', 0, 0)
        self.timezone = timezone

        self._balance = float(initial_balance)  # force use of floats here, but maybe Decimal would be better

    @property
    def account_number(self):
        return self._account_number

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self.validate_and_set_name('_first_name', value, 'First Name')

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self.validate_and_set_name('_last_name', value, 'Last Name')

    # also going to create a full_name computed property, for ease of use
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def timezone(self):
        return self._timezone

    @property
    def balance(self):
        return self._balance

    @timezone.setter
    def timezone(self, value):
        if not isinstance(value, TimeZone):
            raise ValueError('Time zone must be a valid TimeZone object.')
        self._timezone = value

    @classmethod
    def get_interest_rate(cls):
        return cls._interest_rate

    @classmethod
    def set_interest_rate(cls, value):
        if not isinstance(value, numbers.Real):
            raise ValueError('Interest rate must be a real number')
        if value < 0:
            raise ValueError('Interest rate cannot be negative.')
        cls._interest_rate = value

    def validate_and_set_name(self, property_name, value, field_title):
        if value is None or len(str(value).strip()) == 0:
            raise ValueError(f'{field_title} cannot be empty.')
        setattr(self, property_name, value)


# try:
#         a = Account('12345', 'John', '')
# except ValueError as ex:
#         print(ex)
#
# a = Account('12345', 'Alex', 'Martelli')
# print(a.first_name, a.last_name, a.full_name)
#
# try:
#     a = Account('123', 'John', 'Smith',  initial_balance=100)
# except ValueError as ex:
#     print(ex)
#
# a = Account('123', 'John', 'Smith')
# print(a.timezone)
a1 = Account(1234, 'Monty', 'Python', initial_balance=0)
a2 = Account(2345, 'John', 'Cleese', initial_balance=0)
print(a1.interest_rate, a2.interest_rate)

try:
    a1.balance = 200
except AttributeError as ex:
        print(ex)


