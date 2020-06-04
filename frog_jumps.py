# A frog jumps #4

# A frog wants to cross the road.
# The frog is currently located at position X
# and wants to get to a position greater than or equal to Y.
# The small frog always jumps a fixed distance, D.


def solution(X, Y, D):
    distance = Y - X
    if distance % D == 0:
        return distance // D
    return distance // D + 1
