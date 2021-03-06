# Quicksort in python
def Quicksort(A, l, r):
    if r-l <= 1: # Base Case
        return ()

    # Partition with request to print, a[l]
    yellow = l + 1

    for green in range(l+1, r):
        if A[green] <= A[l]:
            (A[yellow], A[green]) = (A[green], A[yellow])
            yellow = yellow + 1

    # Move Pivot into place
    (A[l], A[yellow-1]) = (A[yellow-1], A[l])

    Quicksort(A, l, yellow-1)
    Quicksort(A, yellow, r)

LIST = list(range(10, 0, -1))
Quicksort(LIST, 0, len(LIST))
