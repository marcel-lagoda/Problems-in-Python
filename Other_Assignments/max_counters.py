# You are given N counters, initially set to 0,
# and you have two possible operations on them:

# increase(X) − counter X is increased by 1,
# max counter − all counters are set to the maximum value of any counter.
# A non-empty array A of M integers is given.
# This array represents consecutive operations:
# 
# if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
# if A[K] = N + 1 then operation K is max counter.

# For example, given integer N = 5 and array A such that:
# 
#     A[0] = 3
#     A[1] = 4
#     A[2] = 4
#     A[3] = 6
#     A[4] = 1
#     A[5] = 4
#     A[6] = 4
# the values of the counters after each consecutive operation will be:
# 
#     (0, 0, 1, 0, 0)
#     (0, 0, 1, 1, 0)
#     (0, 0, 1, 2, 0)
#     (2, 2, 2, 2, 2)
#     (3, 2, 2, 2, 2)
#     (3, 2, 2, 3, 2)
#     (3, 2, 2, 4, 2)
# The goal is to calculate the value of every counter after all operations.


A = [3, 4, 4, 6, 1, 4, 4]
N = 5

def solution(N, A):
    counters= [0] * N  # The list to be returned
    start_line = 0  # The used value in previous max_counter command
    current_max = 0  # The current maximum value of any counter
    
    for i in A:
        x = i - 1
        if i > N:
            start_line = current_max
        elif counters[x] < start_line:
            counters[x] = start_line + 1
        else:
            counters[x] += 1
        
        if i <= N and counters[x] > current_max:
            current_max = counters[x]
            
    for i in range(0, len(counters)):
        if counters[i] < start_line:
            counters[i] = start_line
    
    return counters

# 2

def solution2(N, A):
    result = [0] * N  # The list to be returned
    max_counter = 0  # The value in previous max_counter command
    current_max = 0  # The current maximum value of any counter
    
    for i in A:
        if 1 <= i <= N:
            if max_counter > result[i - 1]:
                result[i - 1] = max_counter
            result[i - 1] += 1
            if current_max < result[i - 1]:
                current_max = result[i - 1]
        else:
            max_counter = current_max
            
    for index in range(0, N):
        if result[index] < max_counter:
            result[index] = max_counter
            
    return result
    



# --------------------

print(solution(N, A))
print(solution2(N, A))