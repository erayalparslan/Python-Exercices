"""
    Write a short Python function, is_multiple(n, m), that takes two integer
    values and returns True if n is a multiple of m, that is, n = mi for some
    integer i, and False otherwise
"""


def is_multiple(n, m):
    if m == 0:
        return False
    return n % m == 0


# print is_multiple(10, 2)
# print is_multiple(10, 3)


##############################################################################


"""
    Write a short Python function, is_even(k), that takes an integer value and
    returns True if k is even, and False otherwise. However, your function
    cannot use the multiplication, modulo, or division operators.
"""


def is_even(k):
    if type(k) is not int:
        print "{} is not integer.".format(k)
        return False
    return k & 1 == 0


# print is_even(23)
# print is_even(22)

