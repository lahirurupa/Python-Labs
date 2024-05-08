def QUICKSORT(A, p, r):
    if p < r:
        q = PARTITION(A, p, r)
        QUICKSORT(A, p, q - 1)
        QUICKSORT(A, q + 1, r)


def PARTITION(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def calculate_stats(A):
    n = len(A)
    # Sort the array
    QUICKSORT(A, 0, n - 1)
    print("Sorted Array:", A)

    # Range
    array_range = A[-1] - A[0]
    print("Range:", array_range)

    # Median
    if n % 2 == 0:
        median = (A[n // 2 - 1] + A[n // 2]) / 2
    else:
        median = A[n // 2]
    print("Median:", median)

    # Average
    average = sum(A) / n
    print("Average:", average)


A = []
for _ in range(5):
    A.append(float(input("Enter a number: ")))

calculate_stats(A)