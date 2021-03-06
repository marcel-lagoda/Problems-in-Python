# A binary gap

#  A binary gap within a positive integer N is any maximal sequence of consecutive zeros
#  that is surrounded by ones at both ends in the binary representation of N.
#  For example, number 9 has binary representation 1001 and contains a binary gap of length 2.
#  The number 529 has binary representation 1000010001 and contains two binary gaps:
#  one of length 4 and one of length 3.
#  The number 20 has binary representation 10100 and contains one binary gap of length 1.
#  The number 15 has binary representation 1111 and has no binary gaps.
#  The number 32 has binary representation 100000 and has no binary gaps.
#  Write a function
#  that, given a positive integer N, returns the length of its longest binary gap.
#  The function should return 0 if N doesn't contain a binary gap.
#  For example, given N = 1041 the function should return 5,
#  because N has binary representation 10000010001 and so its longest binary gap is of length 5.
#  Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.

#  Write an efficient algorithm for the following assumptions:
#  N is an integer within the range [1..2,147,483,647].

# 9    = '1001'      --> max gap = 2
# 529  = '100010001' --> max gap = 3
# 20   = '10100'     --> max gap = 1
# 15   = '1111'      --> max gap = 0
# 32   = '100000'    --> max gap = 0
# 1041 = '1000001000'--> max gap = 5


def solution(N):
    """
    Convert a positive integer into a binary.
    Count all '0' placed between 1.
    :param N: positive int
    :return: size of binary gap
    """
    # binary = '{0:b}'.format(N)
    binary = bin(N)[2:]
    maxi = max(binary.strip('0').split('1'))
    return maxi.count('0')


def solution2(N):
    """
    Convert a positive integer into a binary.
    Count all '0' placed between 1.
    :param N: positive int
    :return: size of binary gap
    """
    return len(max(format(N, 'b').strip('0').split('1')))


#  --------------------------------------------------------

print(solution(9))
print(solution(32))
print(solution(15))
print(solution(1041))
print('---------------------------------------------------')
print(solution2(9))
print(solution2(32))
print(solution2(15))
print(solution2(1041))
