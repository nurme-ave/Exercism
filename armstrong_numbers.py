"""
Determine whether a number is an Armstrong number.

An Armstrong number is a number that is the sum of
its own digits each raised to the power of the number of digits.

EXAMPLES:

153 is an Armstrong number, because: 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
154 is not an Armstrong number, because: 154 != 1^3 + 5^3 + 4^3 = 1 + 125 + 64 = 190
"""


def is_armstrong_number(number):
    num_of_digits = len(str(number))    # get the length of digits in number
    list_of_integers = [int(num) for num in str(number)]    # create a list of integers of those digits

    # get the sum of its own digits each raised to the power of the number of digits.
    sum_of_digits = sum([num ** num_of_digits for num in list_of_integers])

    return sum_of_digits == number
