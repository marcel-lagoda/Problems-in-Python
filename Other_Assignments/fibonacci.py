# Fibonacci Sequence

def solution(maxi):
    """
    Return Fibonacci Sequence
    :return: a list
    """
    # initialize variables
    a = 1
    b = 1
    # c = 0
    fib = []

    # append empty list with generated numbers
    while a < maxi:
        c = a + b
        fib.append(a)  # extra
        a = b
        b = c

    return fib, a


# print(solution(1000))


# -------------

def fibonacci(maxi):
    """
    Generate fib. sequence.
    :param maxi: int
    :return: iterator
    """
    next, current = 1, 0
    while next < maxi:
        current, next = next, next + current
        yield current


# print(list(fibonacci(1000)))

# ----------------------------


def fib(number):
    """
    Calculate value of nth Fibonacci number
    :param number: int
    :return: int
    """
    if number <= 1:
        return 0
    elif number == 2:
        return 1
    else:
        n_1 = fib(number - 1)
        n_2 = fib(number - 2)
        n = n_1 + n_2
        return n


print(fib(7))
