# Cyclic rotation

# An array A consisting of N integers is given.
# Rotation of the array means that each element is shifted right by one index,
# and the last element of the array is moved to the first place.
# For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7]
# (elements are shifted right by one index and 6 is moved to the first place).
#
# The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.
# Write a function:
# that, given an array A consisting of N integers and an integer K, returns the array A rotated K times.
#
# For example, given
#
#     A = [3, 8, 9, 7, 6]
#     K = 3
# the function should return [9, 7, 6, 3, 8]. Three rotations were made:
#
#     [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
#     [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
#     [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
# For another example, given
#
#     A = [0, 0, 0]
#     K = 1
# the function should return [0, 0, 0]
#
# Given
#     A = [1, 2, 3, 4]
#     K = 4
# the function should return [1, 2, 3, 4]
#
# Assume that:
# N and K are integers within the range [0..100];
# each element of array A is an integer within the range [−1,000..1,000].
# In your solution, focus on correctness.
# The performance of your solution will not be the focus of the assessment.


def solution(A, K=7):
    if len(A) == 0:
        return A
    K %= len(A)
    return A[-K:] + A[:-K]


def solution_2(A, K=2):
    return A[len(A) - K: len(A)] + A[0: len(A) - K]


def solution_3(A, K=2):
    old = A
    new = [0] * len(A)

    for i in range(K):
        new[0] = old[-1]
        new[1:] = old[:-1]
        old = new[:]
    return new


def solution_4(A, K):
    if len(A) == 0:
        return A

    result = [None] * len(A)

    for i in range(len(A)):
        result[(i + K) % len(A)] = A[i]

    return result


A = [3, 8, 9, 7, 6]

# --------------------------

print(A)
print('--------------------------')

print(solution(A))
print(solution_2(A))
print(solution_3(A))
print(solution_4(A, 2))
