import math
execfile('Sorting/counting-sort/csort.py')

def radix_int_sort(A, digits):
    for d in range(digits):
        sortable = []
        for a in A:
            sortable.append([int(math.floor(a % 10**(d+1) / 10**(d))), a])
        A = csort_radix(sortable, [0,9])

    return A
