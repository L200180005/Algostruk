def bubbleSort(arr):
    n = len(arr)
    for i in range (n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr
def gabung(a,b):
    c = []
    c = a+b
    n = len(c)
    for i in range(n):
        for j in range(0, n-i-1):
            if c[j] > c[j+1] :
                c[j], c[j+1] = c[j+1], c[j]
    return c
