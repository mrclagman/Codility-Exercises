'''
A non-empty zero-indexed array A consisting of N integers is given. Array A represents numbers on a tape.
Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].
The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|
In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

For example, consider array A such that:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
We can split this tape in four places:

P = 1, difference = |3 − 10| = 7
P = 2, difference = |4 − 9| = 5
P = 3, difference = |6 − 7| = 1
P = 4, difference = |10 − 3| = 7
Write a function:

    def solution(A)

that, given a non-empty zero-indexed array A of N integers, returns the minimal difference that can be achieved.
'''

def solution(A):

    # initialize leftSum as the first element of the array A
    # then rightSum as the sum of the remaining elements of array A
    leftSum  = A[0]
    rightSum = sum(A[1:])

    # diff is the value of the difference of the sums
    # lowDiff is the current lowest difference between the two sums
    diff    = abs(leftSum - rightSum)
    lowDiff = diff

    # for every element in the array
    # update the sum by adding current element to leftSum
    # and subtracting current element from rightSumf
    for i in range(1, len(A)-1):
        leftSum  = leftSum  + A[i]
        rightSum = rightSum - A[i]

        diff  = abs(leftSum - rightSum)

        if lowDiff > diff:
            lowDiff = diff

    return lowDiff



if __name__ == "__main__":
    A = [3,1,2,4,3]
    print solution(A)
