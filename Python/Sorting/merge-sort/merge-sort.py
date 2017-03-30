def merge_sort(A):
    #
    # Sorting Algorithm
    # Time Complexity:    O(n lg n)
    # Space Complexity:   O(n)

    if(len(A) == 1):
        return A
    left = A[:len(A)/2]
    right = A[len(A)/2:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(l1, l2):
    m = []
    while(len(l1) > 0 and len(l2) > 0):
        if(l1[0]<l2[0]):
            m.append(l1.pop(0))
        else:
            m.append(l2.pop(0))
    while(len(l1) > 0):
        m.append(l1.pop(0))
    while(len(l2)>0):
        m.append(l2.pop(0))
    return m
