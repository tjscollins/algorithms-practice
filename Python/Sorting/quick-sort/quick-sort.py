import random

def qsort(A):
    #
    # Sorting Algorithm
    # Time Complexity:    O(n^2), O(n lg n) average
    # Space Complexity:   O(n)

    if(len(A) <= 1):
        return A
    (left, mid, right) = partition(A, random.randrange(0, len(A)))
    return qsort(left) + mid + qsort(right)

def partition(A, i):
    pivot = A[i]
    left, mid, right = [], [], []
    for a in A:
        if(a<pivot):
            left.extend([a])
        elif(a>pivot):
            right.extend([a])
        else:
            mid.extend([a])
    return (left, mid, right)
