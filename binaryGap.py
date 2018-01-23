'''
Write a function:

    def solution(N)

that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.
For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5.


'''

def solution(N):
    # convert integer N to binary in array form
    arr = [int(x) for x in bin(N)[2:]]

    # number of occurence of 0 after 1 digit
    gapCount = 0

    # longest gap as of date
    longGap  = 0

    # traverse the array containing the binary representation of N
    for i in arr:
        if i == 0:
            gapCount = gapCount + 1
        else:
            if longGap < gapCount:
                longGap = gapCount
            gapCount = 0
    return longGap



if __name__ == "__main__":
    print solution(6)
    print solution(20)
    print solution(10)
