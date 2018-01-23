'''
A zero-indexed array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one index, and the last element of the array is moved to the first place. For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one index and 6 is moved to the first place).
The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.



Write a function:

def solution(A, K)

that, given a zero-indexed array A consisting of N integers and an integer K, returns the array A rotated K times.

For example, given

    A = [3, 8, 9, 7, 6]
    K = 3
the function should return [9, 7, 6, 3, 8]. Three rotations were made:
    [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
    [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
    [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
'''


def solution(A, K):
    # initialize an array of 0s. This will serve as the array of the rotated input
    sol = [0] * len(A)


    for i in range(len(A)):
        # if current index + K is greater than the length of the array
        # get the difference from the length of the array
        # this will serve as the index of the current element in the new array

        if i + K >= len(A):
            b = (i + K) - len(A)
            sol[b] = A[i]
        else :
            sol[i + K] = A[i]

    return sol

if __name__ == "__main__":
    a = [3, 8, 9, 7, 6]
    k = 3
    print solution(a, k)
