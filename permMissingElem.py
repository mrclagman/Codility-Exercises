'''
A zero-indexed array A consisting of N different integers is given.
The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

    def solution(A)

that, given a zero-indexed array A, returns the value of the missing element.
'''

def solution(A):
    '''
    Since A contains exactly 1 missing element, we get the sum of numbers from 1 to (length of array A + 1).
    Then, we get the sum of the elements in array A.
    The difference of the two sums will net us the missing element
    '''

    b = range(1, len(A) + 2)
    return sum(b) - sum(A)


if __name__ == "__main__":
    A = [2,3,1,5]
    print solution(A)
