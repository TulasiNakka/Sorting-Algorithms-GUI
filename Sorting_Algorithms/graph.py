import time
import numpy as np
import matplotlib.pyplot as plt


#########################################
## Selection Sort #######################
def compare():

    ##################### Merge Sort ###########################
    def merge(arr, low, mid, high):
    
        p = low
        q = mid + 1
        merge_array = []

        for i in range(low, high+1):
            if p > mid:
                merge_array.append(arr[q])
                q+=1
            elif q > high:
                merge_array.append(arr[p])
                p+=1
            elif arr[p] < arr[q]:
                merge_array.append(arr[p])
                p+=1
            else:
                merge_array.append(arr[q])
                q+=1

        for p in range(len(merge_array)):
            arr[low] = merge_array[p]
            low += 1

    def merge_sort(arr, low, high):
        #start=time.time()
        if low < high:
            mid = int((low + high) / 2)

            #Sorting left and right parts
            merge_sort(arr, low, mid)
            merge_sort(arr, mid+1, high)

            merge(arr, low, mid, high)
    
    ################### HEAP SORT ######################

    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[i] < arr[l]:
            largest = l
        if r < n and arr[largest] < arr[r]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    def heap_sort(arr):
        n = len(arr)
        for i in range(n, -1, -1):
            heapify(arr, n, i)
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            heapify(arr, i, 0)

     ######################### Quick Sort ###########################
    def quick_sort(arr, start, end):
        if end - start > 1:
            # partioning index
            p = partition(arr, start, end)

            # sorting elements before and after partition
            quick_sort(arr, start, p)
            quick_sort(arr, p + 1, end)

    def partition(arr, start, end):
        pivot = arr[start]   # lowest element
        i = start + 1
        j = end - 1
        while True:
            while (i <= j and arr[i] <= pivot):
                i = i + 1
            while (i <= j and arr[j] >= pivot):
                j = j - 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                arr[start], arr[j] = arr[j], arr[start]

                return j
    

     ####################### QUICK SORT MEDIAN ###############################
    def check_median(M, e, f):
        mid = (e + f - 1) // 2
        a = M[e]
        b = M[mid]
        c = M[f - 1]
        if a <= b <= c:
            return b, mid
        if c <= b <= a:
            return b, mid
        if a <= c <= b:
            return c, e - 1
        if b <= c <= a:
            return c, f - 1
        return a, e

    def qsm(L, start, end, asc=True):
        result = 0
        if start < end:
            pivot_location, result = Partition(L, start, end, asc)
            result += qsm(L, start, pivot_location, asc)
            result += qsm(L, pivot_location + 1, end, asc)
        return result

    def Partition(L, start, end, asc=True):
        result = 0
        pivot, pida = check_median(L, start, end)
        L[start], L[pida] = L[pida], L[start]
        i = start + 1
        for j in range(start + 1, end, 1):
            result += 1
            if (asc and L[j] < pivot) or (not asc and L[j] > pivot):
                L[i], L[j] = L[j], L[i]
                i += 1
        L[start], L[i - 1] = L[i - 1], L[start]
        return i - 1, result

    def quicksort_median(l, asc=True):
        qsm(l, 0, len(l), asc)

    ################### Insertion Sort #######################
    def insertionSort(arr):
        for i in range(1, len(arr)):
            element = arr[i]
            j = i-1
            while (j >=0 and element < arr[j]):
                arr[j+1] = arr[j]
                j -= 1               
            arr[j+1] = element


    ###################### SELECTION SORT #######################
    def selection_sort(arr):
        n=len(arr)
        for i in range(0,n-1):
                for j in range(i+1,n):
                    if (arr[i]>arr[j]):
                        arr[i], arr[j] = arr[j], arr[i]  #SWAP


########################### BUBBLE SORT ##########################
    def bubble_sort(arr):
        n=len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if (arr[j] > arr[j + 1]):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j] 

    ###################### DONE ##############################
    
    ######################## TO GENERATE GRAPH #################################
    #Declared the name and function using lambda concept
    sorts = [
        {
            "name": "Merge Sort",
            "sort": lambda arr: merge_sort(arr, 0, len(arr) - 1),
            "Complexity": "O(N log N)"
        },
        {
            "name": "Heap Sort",
            "sort": lambda arr: heap_sort(arr),
            "Complexity": "O(N log N)"
        },
        {
            "name": "Quick Sort",
            "sort": lambda arr: quick_sort(arr, 0, len(arr) - 1),
            "Complexity": "O(N log N)"
        },
        {
            "name": "Quick Sort 3 Medians",
            "sort": lambda arr: quicksort_median(arr),
            "Complexity": "O(N log N)"
        },
        {
            "name": "Insertion Sort",
            "sort": lambda arr: insertionSort(arr),
            "Complexity": "O(N^2)"
        },
        {
            "name": "Selection Sort",
            "sort": lambda arr: selection_sort(arr),
            "Complexity": "O(N^2)"
        },
        {
            "name": "Bubble Sort",
            "sort": lambda arr: bubble_sort(arr),
            "Complexity": "O(N^2)"
        },
    ]

    elements = np.array([i*1000 for i in range(1, 10)])

    plt.xlabel('List Length')
    plt.ylabel('Time Complexity')

    for sort in sorts:
        times = list()
        start_all = time.time()
        for i in range(1, 10):
            start = time.time()
            a = np.random.randint(1000, size = i * 1000)
            sort["sort"](a)
            high = time.time()
            times.append(high - start)

            print(sort["name"], "Sorted", i * 1000, "Elements in", high - start, "s")
            
        high_all = time.time()
        print(sort["name"], "Sorted Elements in", high_all - start_all, "s")

        plt.plot(elements, times, label = sort["name"] +'-' + sort["Complexity"] )
        

    plt.grid()
    plt.legend()
    plt.show()

if __name__ == '__main__':
    compare()
    