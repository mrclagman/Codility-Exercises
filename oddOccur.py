'''
Write a function:

    def solution(A)

that, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.
For example, given array A such that:
  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the function should return 7, as explained in the example above.
'''


def solution(A):
    # declare a zero array with same length A
    # this serves as a flag if current element is paired or not
    flag = [0] * len(A)

    for i in xrange(len(A)):

        # check next elements of the array until to its last element
        for b in range(i + 1, len(A)):

            # if current element has a match on remaining elements of the array and is unpaired
            # set its flag to 1 to signify it it paired
            # then move to the next element
            if A[i] == A[b] and flag[i] == 0:
                flag[i] = 1
                flag[b] = 1
                break;

    # find the element with flag = 0, which is the unpaired element
    zero_idx = flag.index(0)
    return A[zero_idx]

if __name__ == "__main__":
    A = [9,3,9,3,9,7,9]
    print solution(A)
