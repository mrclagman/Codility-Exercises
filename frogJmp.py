'''
A small frog wants to get to the other side of the road. The frog is currently located at position X and wants to get to a position greater than or equal to Y. The small frog always jumps a fixed distance, D.
Count the minimal number of jumps that the small frog must perform to reach its target.

Write a function:
    def solution(X, Y, D)

that, given three integers X, Y and D, returns the minimal number of jumps from position X to a position equal to or greater than Y.
'''


def solution(X, Y, D):
    dist = Y - X
    if dist % D == 0:
        return dist / D
    else:
        return (dist / D) + 1


if __name__ == "__main__":
    print solution(10, 85, 30)
    print solution(10, 40, 30)
