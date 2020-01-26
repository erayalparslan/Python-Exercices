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


"""
    Write a short Python function that takes a positive integer n and returns
    the sum of the squares of all the odd positive integers smaller than n.
"""


def sumOfOddSquares(n):
    if n <= -1:
        print('input must be positive')
    else:
        total = 0
        for i in range(1,n):
            if i % 2 == 1:
                total += i*i
        return total
        
        
# print(sumOfOddSquares(4))


##############################################################################


"""
    Give a single command that computes the sum from Exercise R-1.6, 
    relying on Python’s comprehension syntax and the built-in sum function
"""


def sumOfOddSquaresWithSingleCommand(n):
    if n <= -1:
        print('input must be positive')
    else:
        return (sum(x*x for x in range(1,n) if x % 2 == 1))
        
        
# print(sumOfOddSquaresWithSingleCommand(4))


##############################################################################


"""
    Demonstrate how to use Python’s list comprehension syntax to produce
    the list [ a , b , c , ..., z ], but without having to type all 26 such
    characters literally
"""


def printAllEnglishLetters():
    for i in range(26):
        if i == 25: print(chr(i+97), end='')
        else: print(chr(i+97), end=', ')


# printAllEnglishLetters()


##############################################################################


"""
    Write a Python program that repeatedly reads lines from standard input
    until an EOFError is raised, and then outputs those lines in reverse order
    (a user can indicate end of input by typing ctrl-D).
"""


def read_file(filepath):
    fp = open(filepath)
    lines = []
    
    while True:
        try:
            line = fp.readline()
            if line == '': 
                raise EOFError
            else:
                lines.append(line[:-1])
        except EOFError:
            for line in lines.reversed():
                print(line)
            return
        
        
##############################################################################


"""
    Write a short Python program that takes two arrays a and b of length n
    storing int values, and returns the dot product of a and b. That is, it returns
    an array c of length n such that c[i] = a[i] · b[i], for i = 0,...,n−1.
"""


def product(firstList, secondList):
    if not isinstance(firstList, list) or not isinstance(secondList, list):
        print('input(s) are not list')
    elif len(firstList) != len(secondList):
        print('lengths of the lists do not match!')
    else:
        length = len(firstList)
        newList = []
        for i in range(length):
            newList.append(firstList[i]*secondList[i])
        return newList
    

firstList  = [10,20,30,40,50]
secondList = [1,2,3,4,5]

# print(product(firstList, secondList))


##############################################################################
