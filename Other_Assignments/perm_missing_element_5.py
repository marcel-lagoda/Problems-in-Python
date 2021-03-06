# Find the missing element in the given permutation


# An array A consisting of N different integers is given.
# The array contains integers in the range [1..(N + 1)],
# which means that exactly one element is missing.
# Your goal is to find that missing element.
#
# Write a function that, given an array A, returns the value of the missing element.
#
# For example, given array A such that:
#
#   A[0] = 2
#   A[1] = 3
#   A[2] = 1
#   A[3] = 5
# the function should return 4, as it is the missing element.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [0..100,000];
# the elements of A are all distinct;
# each element of array A is an integer within the range [1..(N + 1)].


A = [1, 2, 3, 5, 6, 7, 8]
B = [3, 2, 1, 8, 7, 6, 5]


# XOR(1)

def solution(A):
    length = len(A)
    xor_sum = 0
    for index in range(0, length):
        xor_sum = xor_sum ^ A[index] ^ (index + 1)
    return xor_sum ^ (length + 1)


# 1. Xor all array elements.
# 2. Xor the whole range (1, n + 1)

#
# def solution_2(A):
#     A.sort()
#     xor = 0
#     xor_2 = 0
#
#     for i in A:
#         xor ^= i
#         for j in range(1, A[-1] + 1):
#             xor_2 ^= j
#     sum_xor = xor_2 ^ xor
#     return sum_xor
#

# SUM FORMULA

# missing_element = (sum of numbers from 1 to n) - (sum of all elements)
# sum of numbers from 1 to n: n*(n+1)/2
# sum of all numbers in the array


# n = a[-1] || n = a.pop()
# sum_n = n * (n + 1) // 2


def solution_sum_formula(A):
    #    A.sort()
    sum_a = sum(A)
    #  n = A[-1]   nie mogę dać n jako ostatniego elementu, bo zwróci błąd dla A[]
    # jeśli usunę A[-1] to mogę też skasować A.sort()
    n = len(A) + 1
    return (n * (n + 1) // 2) - sum_a


# SET DIFFERENCE METHOD
# WORKS BUT NOT THE MOST OPTIMAL SOLUTION

def solution_4(A):
    return min(set(range(1, len(A) + 1)).difference(set(A)))


# ---------------------------

print(solution(A))
print(solution_2(A))
print(solution_2(B))
print('--------sum_formula-----------')
print(solution_sum_formula(A))
print(solution_sum_formula(B))
print(solution_sum_formula([1, 2, 3, 5]))
print(solution_sum_formula([1, 2, 3, 4, 5, 6, 7, 8]))
print(solution_sum_formula([]))
print('-------------------------------')
print(solution_4(A))
print(solution_4(B))
