from time import time as detak
from random import shuffle as kocok
k = [i for i in range(1,6001)]
kocok(k)
def u_bub(arr):
    n = len (arr)
    for i in range (n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
def u_sel(A):
    for i in range(len(A)):
        min_in = i
        for j in range(i+1, len (A)):
            if A[min_in] > A[j]:
                    min_in = j
        A[i], A[min_in] = A[min_in], A[i]
def u_ins(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
