"""Functions for calculating steps in exchanging currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""



def exchange_money(budget, exchange_rate):
    """

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """

    return  budget / exchange_rate
print(f"The exchanged value is: {exchange_money(127.5, 1.20)}")

def get_change(budget, exchanging_value):
    """

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """

    return budget - exchanging_value
print(f"The left of your budget is: {get_change(127.5, 120)}")

def get_value_of_bills(denomination, number_of_bills):
    """

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - total number of bills.
    :return: int - calculated value of the bills.
    """
    
    return number_of_bills * denomination
print(f"the value of your bills is: {get_value_of_bills(5,128)}")

def get_number_of_bills(amount, denomination):
    """

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.
    """

    return amount // denomination
print(f"the number of bills is: {get_number_of_bills(127.5,5)}")

def get_leftover_of_bills(amount, denomination):
    """

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.
    """

    numb_bills = amount // denomination
    return amount - (numb_bills * denomination)
print(f"the left ofover from your number of bills is: {get_leftover_of_bills(127.5,20)}")
    

def exchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    spread_decimal = spread / 100
    real_rate = exchange_rate * (1 + spread_decimal)
    exchang_amount = budget / real_rate
    number_of_bills = int(exchang_amount // denomination)
    exchangeable_value = number_of_bills * denomination
    return exchangeable_value
print(f"The maximum value you can get from this exchange is: {exchangeable_value(127.5, 1.20, 10, 20)}")
    