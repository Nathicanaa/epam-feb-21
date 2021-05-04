"""
You are given the following code:
class Order:
    morning_discount = 0.25
    def __init__(self, price):
        self.price = price
    def final_price(self):
        return self.price - self.price * self.morning_discount
Make it possible to use different discount programs.
Hint: use strategy behavioural OOP pattern.
https://refactoring.guru/design-patterns/strategy
Example of the result call:
def morning_discount(order):
    ...
def elder_discount(order):
    ...
order_1 = Order(100, morning_discount)
assert order_1.final_price() == 50
order_2 = Order(100, elder_discount)
assert order_1.final_price() == 10
"""
from abc import ABC, abstractmethod
from typing import Union


class Strategy(ABC):
    """
    Abstract class for further created strategies
    """

    @abstractmethod
    def final_price(self):
        """
        Abstract method which guarantees that all children will be have this method
        """
        pass


class MorningDiscount(Strategy):
    """
    A strategy for morning discounts
    for this example morning discount is 50%
    """

    def final_price(self) -> float:
        """
        Calculates final price with particular discount
        Returns: final price with discount
        """
        return self.price - self.price * 0.5


class ElderDiscount(Strategy):
    """
    A strategy for elder discounts
    for this example elder discount is 90%
    """

    def final_price(self) -> float:
        """
        Calculates final price with particular discount
        Returns: final price with discount
        """
        return self.price - self.price * 0.9


class Order:
    """
    Context class which works with strategies and provides common interface for them
    """

    def __init__(self, price: Union[int, float], strategy: Strategy):
        """
        Initialises an Order class instance
        Args:
            price: some price
            strategy: chosen strategy
        """
        self.price = price
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        """
        Returns: current strategy
        """
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """
        Provides changing strategy
        Args:
            strategy: a new strategy to change
        """
        self._strategy = strategy

    @staticmethod
    def check_int(price: float) -> Union[int, float]:
        """
        Checks number, if number can be int it converts it int
        otherwise returns initial float
        Args:
            price: some float
        Returns: int if possible, float otherwise
        """
        if price - round(price) == 0:
            return int(price)
        return price

    def final_price(self) -> float:
        """
        Calculates a final price with a chosen discount strategy
        Returns: a final price with discount
        """
        return self.check_int(self._strategy.final_price(self))
