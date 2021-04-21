# A test for homework11 task2
from homework11.tasks.task2 import ElderDiscount, MorningDiscount, Order

order1 = Order(100, ElderDiscount)
order2 = Order(1000, MorningDiscount)


def test_final_prices():
    """
    Passes if final price calculates correctly
    """
    assert order1.final_price() == 10
    assert order2.final_price() == 500


def test_price():
    """
    Passes if prices are equal to expected
    """
    assert order1.price == 100
    assert order2.price == 1000


def test_strategy():
    """
    Passes if strategy properties are equal to expected
    """
    assert order1.strategy == ElderDiscount
    assert order2.strategy == MorningDiscount


def test_change_strategy():
    """
    Passes if strategies changed successfully
    """
    order1.strategy = MorningDiscount
    assert order1.strategy == MorningDiscount
    assert order1.final_price() == 50
    order2.strategy = ElderDiscount
    assert order2.strategy == ElderDiscount
    assert order2.final_price() == 100
