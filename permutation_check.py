# A non-empty array A consisting of N integers is given.
# 
# A permutation is a sequence containing each element from 1 to N once,
# and only once.
# 
# For example, array A such that:
# 
#     A[0] = 4
#     A[1] = 1
#     A[2] = 3
#     A[3] = 2
# is a permutation, but array A such that:
# 
#     A[0] = 4
#     A[1] = 1
#     A[2] = 3
# is not a permutation, because value 2 is missing.
# 
# The goal is to check whether array A is a permutation.

A = [1, 2, 3, 4]
B = [1, 3, 4, 5]


def solution(A):
    counter = [0] * len(A)
    limit = len(A)
    
    for i in A:
        if not 1 <= i <= limit:
            return 0
        else:
            if counter[i - 1] != 0:
                return 0
            else:
                counter[i - 1] = 1
    return 1


# ---------------------------

print(solution(A))
print(solution(B))
