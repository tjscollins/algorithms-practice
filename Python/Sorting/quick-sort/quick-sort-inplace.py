import random

def qsort_inplace(A):
    #
    # Sorting Algorithm
    # Time Complexity:    O(n^2), O(n lg n) average
    # Space Complexity:   O(1)
    if(len(A) <= 1):
        return A
    A, l, r = partition_inplace(A, random.randrange(0, len(A)))
    return qsort(A[:l]) + A[l:r] + qsort(A[r:])

def partition_inplace(A, i):
    pivot = A[i]
    l, m, r = 0,0,len(A)
    while m<r:
        if(A[m] < pivot):
            A[m], A[l] = A[l], A[m]
            m += 1
            l += 1
        elif(A[m] == pivot):
            m+= 1
        else:
            r-=1
            A[m], A[r] = A[r], A[m]
    return A, l, r
