#!/usr/bin/python

import math

def sort_the_files(n, result):
    # Write your solution here
    files = []
    for i in range(n, 0, -1):
        files.append([i, 'IMG' + str(i) + '.jpg'])
    print radix_sort(files)

def radix_sort(files):
    digits = int(math.ceil(math.log(len(files)+1, 10)))
    for d in range(digits-1, -1, -1):
        sortable = []
        for f in files:
            if d-len(f) < 0:
                key = 0
            else:
                key = int(math.floor(f[0] % 10**(d+1) / 10**d))
            sortable.append([key, f])
        files = csort(sortable, [0,9])

    return files

def csort(A, keyRange):
    counts = [None]*(keyRange[1]-keyRange[0]+1)
    for a in A:
        if counts[a[0]-keyRange[0]] is None:
            counts[a[0]-keyRange[0]] = [a]
        else:
            counts[a[0]-keyRange[0]].append(a)
    i = 0
    for j in range(len(counts)):
        if counts[j] is None:
            counts[j] = []
        while len(counts[j]) > 0:
            A[i] = counts[j].pop(0)[1]
            i += 1
    return A

result = []
sort_the_files(100, result)
