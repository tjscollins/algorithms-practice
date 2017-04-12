def selection_sort(A):
    for i in range(len(A)):
        m = i
        for j in range(i, len(A)):
            if A[j]<A[m]:
                m = j
        A[m], A[i] = A[i], A[m]
    return A
