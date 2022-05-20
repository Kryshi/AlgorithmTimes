import random
import math

insertion_swap_count = 0
insertion_comp_count = 0

quick_swap_count = 0
quick_comp_count = 0

heap_swap_count = 0
heap_comp_count = 0

def priprav_pole(a):
    A = []
    for i in range(0,a):
        A.append(random.randint(0,1000))
    return A

def je_neklesajici(A):
    for i in range(len(A)):
        if A[i] > A[i]:
            return False
    return True

def Insertion_sort(A):
    global insertion_swap_count
    global insertion_comp_count
    for j in range(len(A)):
        insertion_comp_count += 1
        t = A[j]
        i = j - 1
        while i >= 0 and A[i] > t:
            A[i + 1] = A[i]
            i = i - 1
            insertion_comp_count += 2
            insertion_swap_count += 1
        A[i + 1] = t
    return A

def Quick_sort(A, p, r):
    global quick_swap_count
    global quick_comp_count
    if p < r:
        quick_comp_count += 1
        q = Partition(A, p, r)
        Quick_sort(A, p, q - 1)
        Quick_sort(A, q + 1, r)
    return A

def Partition(A, p, r):
    global quick_swap_count
    global quick_comp_count
    x = A[r]
    i = p - 1
    for j in range(p,r):
        quick_comp_count += 1
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
            quick_swap_count += 1
            quick_comp_count += 1
    A[i + 1], A[r] = A[r], A[i + 1]
    quick_swap_count += 1
    return i + 1

def Max_heapify(A, n, i):
    global heap_swap_count
    global heap_comp_count

    largest = i 
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and A[largest] < A[l]:
        largest = l
        heap_comp_count += 2
    
    if r < n and A[largest] < A[r]:
        largest = r
        heap_comp_count += 2

    if largest != i:
        heap_comp_count += 1
        A[i], A[largest] = A[largest], A[i]
        heap_swap_count += 1
        Max_heapify(A, n, largest)

def Heap_sort(A):
    global heap_swap_count
    global heap_comp_count

    n = len(A)

    for i in range(n//2, -1, -1):
        heap_comp_count += 1
        Max_heapify(A, n, i)


    for i in range(n-1, 0,-1):
        heap_comp_count += 1
        A[i], A[0] = A[0], A[i]
        heap_swap_count += 1
        Max_heapify(A,i, 0)

    return A

def get_insertion_comp_number(array):
    global insertion_comp_count
    global insertion_swap_count
    insertion_swap_count = 0
    insertion_comp_count = 0
    Insertion_sort(array)
    return insertion_comp_count, insertion_swap_count

def get_quick_comp_number(array):
    global quick_comp_count
    global quick_swap_count
    n = len(array) - 1
    quick_swap_count = 0
    quick_comp_count = 0
    Quick_sort(array, 0, n)
    return quick_comp_count, quick_swap_count

def get_heap_comp_number(array):
    global heap_comp_count
    global heap_swap_count
    heap_swap_count = 0
    heap_comp_count = 0
    Heap_sort(array)
    return heap_comp_count, heap_swap_count

A10 = priprav_pole(10)
A100 = priprav_pole(100)
A1000 = priprav_pole(1000)
A10000 = priprav_pole(10000)

B10 = A10.copy()
B100 = A100.copy()
B1000 = A1000.copy()
B10000 = A10000.copy()

C10 = A10.copy()
C100 = A100.copy()
C1000 = A1000.copy()
C10000 = A10000.copy()

def print_comparison_tables():
    print()
    print("(Počet porovnání - Počet prohození)")
    print("Jméno algoritmu\t""\t""10\t""\t""100\t""\t""1000\t""\t""\t""10000\t")

    print("Insertion sort","\t""\t",get_insertion_comp_number(A10),"\t",get_insertion_comp_number(A100),"\t",get_insertion_comp_number(A1000),"\t",get_insertion_comp_number(A10000))
    print("Quick sort","\t""\t",get_quick_comp_number(B10),"\t",get_quick_comp_number(B100),"\t",get_quick_comp_number(B1000),"\t""\t",get_quick_comp_number(B10000))
    print("Heap sort","\t""\t",get_heap_comp_number(C10),"\t",get_heap_comp_number(C100),"\t",get_heap_comp_number(C1000),"\t""\t",get_heap_comp_number(C10000))


print_comparison_tables()