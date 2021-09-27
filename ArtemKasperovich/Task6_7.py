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
        "USD": 1
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
            return self.value + other * self.currency
        if isinstance(other, Money):
            return self.value + other.value * self.currency

    def __radd__(self, other):
        if isinstance(other, (int, float)):
            return self.value + other * self.currency
        elif isinstance(other, Money):
            return self.value + other.value * self.currency

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return self.value * self.currency - other
        if isinstance(other, Money):
            return self.value - other.value * other.currency

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            return self.value * self.currency - other
        return self.value - other.value * other.currency

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self.value * other/self.currency
        if isinstance(other, Money):
            return self.value * self.currency * other.value * other.currency

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return self.value * other / self.currency
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
        return f'{self.__class__.__name__}(value: {self.value:.2f},currency: {self.currency})'


if __name__ == '__main__':
    x = Money(10, "BYN")
    y = Money(11)
    z = Money(12.34, "EUR")

    print(z + 3.11 * x + y * 0.8)
    print(z + x * 3.11 + y * 0.8)
    print(x != y)
    print(x > y)
    print(x < y)
    print(x == y)
    print(x <= y)
    print(x >= y)
