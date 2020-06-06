# Odd Occurrence in Array

# A non-empty array A consisting of N integers is given.
# The array contains an odd number of elements,
# and each element of the array can be paired with another element that has the same value,
# except for one element that is left unpaired.
#
# For example, in array A such that:
#
#   A[0] = 9  A[1] = 3  A[2] = 9
#   A[3] = 3  A[4] = 9  A[5] = 7
#   A[6] = 9
# the elements at indexes 0 and 2 have value 9,
# the elements at indexes 1 and 3 have value 3,
# the elements at indexes 4 and 6 have value 9,
# the element at index 5 has value 7 and is unpaired.
# Write a function:
# that, given an array A consisting of N integers fulfilling the above conditions,
# returns the value of the unpaired element.
#
# For example, given array A such that:
#
#   A[0] = 9  A[1] = 3  A[2] = 9
#   A[3] = 3  A[4] = 9  A[5] = 7
#   A[6] = 9
# the function should return 7, as explained in the example above.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an odd integer within the range [1..1,000,000];
# each element of array A is an integer within the range [1..1,000,000,000];
# all but one of the values in A occur an even number of times.


def solution(A):
    odd = 0
    for i in A:
        odd ^= i
    return odd


# [3 ^ 9 ^ 3 ^ 9 ^ 3 ^ 2 ^ 3] = 7
# [9 ^ 9 ^ 3 ^ 3 ^ 3 ^ 3 ^ 2] = 7


# .count() niewydajna przy dużych liczbach,
# bo count tworzy tablicę z hashem


def solution_1(A):
    for num in A:
        if A.count(num) % 2:
            return num


def solution_2(A):
    return [num for num in A if A.count(num) % 2]


def solution_3(A):
    return [num for num in set(A) if A.count(num) % 2 != 0][0]


#  ------------------------------------------------------------


def solution_4(A):
    for i in range(len(A)):
        counter = 0
        for j in range(len(A)):
            if A[i] == A[j]:
                counter += 1

        if counter % 2 != 0:
            return A[i]
    return -1


# solution incorrect
# although it might return correct answer when odd is max
#
# def solution_5(A):
#     A.sort()
#     N = len(A)
#     counter = 0
#     while counter < N:
#         try:
#             if A[i] == A[i + 1]:
#                 counter += 2
#             else:
#                 return A[i]
#         except:
#             return A[-1]


A = [3, 9, 3, 9, 3, 1, 3]
print(solution_1(A))
print(solution_2(A))
print(solution_3(A))
print(solution_4(A))
# print("x", solution_5(A))
print(solution(A))
