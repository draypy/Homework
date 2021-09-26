# Task 4.7
# Implement a class Money to represent value and currency.
# You need to implement methods to use all basic arithmetics expressions
# (comparison, division, multiplication, addition and subtraction).
# Tip: use class attribute exchange rate which is dictionary and stores information about exchange rates
# to your default currency:


from functools import total_ordering


@total_ordering
class Money:
    exchange_rate = {
        "EUR": 0.93,
        "BYN": 2.1,
        "USD": 1,
        "UA": 2.9,
        "RUB": 70
    }

    def __init__(self, value, currency='USD'):
        self.value = value
        self.currency = self.exchange_rate[currency]

    def __eq__(self, other):
        if isinstance(other, Money):
            return self.value * self.currency == other.value * other.currency

    def __lt__(self, other):
        if isinstance(other, Money):
            return self.value * self.currency < other.value * other.currency

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return self.value * self.currency + other
        if isinstance(other, Money):
            return self.value * self.currency + other.value * other.currency

    def __radd__(self, other):
        if isinstance(other, (int, float)):
            return self.value * self.currency + other
        return self.value * self.currency + other.value * other.currency

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return self.value * self.currency - other
        if isinstance(other, Money):
            return self.value * self.currency - other.value * other.currency

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            return self.value * self.currency - other
        return self.value * self.currency - other.value * other.currency

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self.value * self.currency * other
        if isinstance(other, Money):
            return self.value * self.currency * other.value * other.currency

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return self.value * self.currency * other
        return self.value * self.currency * other.value * other.currency

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return self.value * self.currency / other
        if isinstance(other, Money):
            return self.value * self.currency / (other.value * other.currency)

    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):
            return self.value * self.currency / other
        return self.value * self.currency / (other.value * other.currency)

    def __repr__(self):
        return f'{self.__class__.__name__}(value: {self.value:.2f},currency: {self.currency!r})'

    def __str__(self):
        return f'{self.value:.2f} {self.currency}'

#
# x = Money(2, "BYN")
# y = Money(5, "EUR")
# z = Money(2)
# print(x)
# print(z + 3.11 * x + y * 0.8)      # 2 * 5 + 3.11* 2 * 2  + 5 * 3*0.8
# print(x + y)  # 2.1 * 2 + 5*0.93 = 8.85
# print(x - y)  # 2.1 * 2 - 5*0.93 = 0.45
# print(x * y)  # 2.1 * 2 * 5*0.93 = 19.53
# print(x / y)  # 2.1 * 2 / 5*2 =
# lst = [Money(10, 'BYN'), Money(10), Money(10, 'EUR')]
# print(sum(lst))
#
# print(x != y)
# print(x > y)
# print(x < y)
# print(x == y)
# print(x <= y)
# print(x >= y)
