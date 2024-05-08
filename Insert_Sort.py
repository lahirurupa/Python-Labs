A = []
for V in range(10):
    A.append(input('Enter a Number : '))
print(A)

def insert_Sort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j-1
        while (i > 0 and A[i] > key):
            A[i+1]=A[i]
            i = i-1
        A[i+1] = key

insert_Sort(A)
print('Sorted Array : ')
for k in range(len(A)):
    print(A[k])
