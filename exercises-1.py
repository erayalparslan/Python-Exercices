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


##############################################################################


"""
    Write a short Python function, minmax(data), that takes a sequence of
    one or more numbers, and returns the smallest and largest numbers, in the
    form of a tuple of length two. Do not use the built-in functions min or
    max in implementing your solution
"""


def minmax(data):
    if len(data) < 1:
        print('your list is empty')
        return(None,None)
    else:
        min = max = data[0]
        for number in data:
            if number > max:
                max = number
            elif number < min:
                min = number
        return(min,max)


mList = [45,11,56,30,90,22]
min, max = minmax(mList)
# print('minimum is: {}'.format(min))
# print('maximum is: {}'.format(max))


##############################################################################


"""
    Write a short Python function that takes a positive integer n and returns
    the sum of the squares of all the positive integers smaller than n.
"""


def sumsquares(n):
    if n <= -1:
        print('input must be positive')
        return
    else:
        return sum((x*x for x in range(1,n)))
    
    
# print(sumsquares(4))
# print(sumsquares(45))


##############################################################################

