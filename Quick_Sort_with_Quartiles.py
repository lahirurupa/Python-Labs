A = []
for y in range(5):
    A.append(int(input("Enter a number: ")))

def QUICKSORT(A, p, r):
    if p < r:
        q = PARTITION(A, p, r)
        QUICKSORT(A, p, q-1)
        QUICKSORT(A, q+1, r)

def PARTITION(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i = i+1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def quartiles_and_mean(A):
    n = len(A)
    q1_index = n // 4
    q2_index = n // 2
    q3_index = 3 * n // 4

    q1 = A[q1_index]
    q2 = A[q2_index]
    q3 = A[q3_index]
    q4 = A[-1]
    iqr = q3 - q1
    mean = sum(A) / n

    return q1, q2, q3, q4, iqr, mean

QUICKSORT(A, 0, len(A)-1)
print("Sorted array:", A)

q1, q2, q3, q4, iqr, mean = quartiles_and_mean(A)
print("Q1:", q1)
print("Q2 (Median):", q2)
print("Q3:", q3)
print("Q4 (Maximum):", q4)
print("Interquartile Range (IQR):", iqr)
print("Mean:", mean)