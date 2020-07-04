# Missing integer

# Write a function that, given an array A of N integers,
# returns the smallest positive integer (greater than 0) that does not occur in A.
# 
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
# 
# Given A = [1, 2, 3], the function should return 4.
# 
# Given A = [−1, −3], the function should return 1.
# 
# Write an efficient algorithm for the following assumptions:
# 
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].

A = [1, 3, 6, 4, 1, 2]

def solution(A):
    return min(set(range(1, len(A) + 1)).difference(set(A)))

def solution2(A):
    return set(range(1, len(A))).difference(set(A))


def solution3(A):
    occur = [False] * (len(A)+1)
    
    for i in A:
        if 1 <= i <= len(A)+1:
            occur[i - 1] = True
            
    for i in range(len(A) + 1):
        if occur[i] == False:
            return i + 1
        
    return -1

    
    
    
    
# ---------------
print(solution(A))
print(solution2(A))
print(solution3(A))