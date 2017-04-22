def csort(A, keyRange):
    counts = [0]*(keyRange[1]-keyRange[0]+1)
    for a in A:
        counts[a-keyRange[0]] += 1
    i=0
    for c in range(len(counts)):
        while counts[c] > 0:
            A[i] = c+1
            counts[c] -= 1
            i += 1
    return A

def csort_radix(A, keyRange):
    # A is array of arrays, a_n = [key digit, value]
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
