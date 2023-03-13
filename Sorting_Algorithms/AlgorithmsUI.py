from tkinter import *
from tkinter import ttk
import time
import random
import numpy as np
from graph import compare
import tkinter.font as tkFont


root = Tk()
root.title("Project 1 Sorting Algorithms")
root.maxsize(1300, 1800)
root.config(bg = "orange")
fontObj = tkFont.Font(size=28)
welcome = Label(root,text="Sorting Algorithms Project",background="black",foreground="white",font=fontObj)
welcome.grid(row=0,column=5,columnspan=10, padx=20,pady=20,ipadx=20,ipady=20)

algorithms= StringVar()
list = ['Merge Sort' , 'Heap Sort','Quick Sort', 'Quick Sort 3 Medians', 'Insertion Sort','Selection Sort' , 'Bubble Sort' ]


arr = []
#RANDOM ARRAY GENERATION BASED ON THE GIVEN ARRAY SIZE FROM GUI
def createArr():
    global arr
    arr = []
    k=arr_name.get()
    for i in range(k):  
        #print(arr_name.get())
        arr.append(np.random.randint(k))
    print(arr)


############################## MERGE SORT FUNCTION #########################################
def merge(arr, begin, mid, end):

    p = begin
    q = mid + 1
    merge_array = []

    for i in range(begin, end+1):
        if p > mid:
            merge_array.append(arr[q])
            q+=1
        elif q > end:
            merge_array.append(arr[p])
            p+=1
        elif arr[p] < arr[q]:
            merge_array.append(arr[p])
            p+=1
        else:
            merge_array.append(arr[q])
            q+=1

    for p in range(len(merge_array)):
        arr[begin] = merge_array[p]
        begin += 1

def merge_sort(arr, begin, end):
    #start=time.time()
    if begin < end:
        mid = int((begin + end) / 2)
        merge_sort(arr, begin, mid)
        merge_sort(arr, mid+1, end)

        merge(arr, begin, mid, end)


#################################### HEAP SORT FUNCTION #############################################
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


############################### QUICK SORT FUNCTION #########################################
def quick_sort(arr, start, end):
    if end - start > 1:
        p = partition(arr, start, end)
        quick_sort(arr, start, p)
        quick_sort(arr, p + 1, end)

def partition(arr, start, end):
    pivot = arr[start]
    i = start + 1
    j = end - 1
    while True:
        while (i <= j and arr[i] <= pivot):   #moving start towards right
            i = i + 1
        while (i <= j and arr[j] >= pivot):   #moving end towards left
            j = j - 1
        if i <= j:                            # checking if start and end have crossed
            arr[i], arr[j] = arr[j], arr[i]   # swapping values to rearrange
        else:
            arr[start], arr[j] = arr[j], arr[start]  #swapping pivot with high so that pivot is at its right position
            return j                                 #returning pivot position


####################### QUICK SORT MEDIAN FUNCTION ###############################
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


####################### INSERTION SORT FUNCTION ###########################
def insertion_sort(arr):
    for i in range(1, len(arr)):
            element = arr[i]
            j = i-1
            while (j >=0 and element < arr[j]):
                arr[j+1] = arr[j]
                j -= 1               
            arr[j+1] = element

######################### SELECTION SORT FUNCTION################################
def selection_sort(arr):
    n=len(arr)
    for i in range(0,n-1):
            for j in range(i+1,n):
                if (arr[i]>arr[j]):
                    arr[i], arr[j] = arr[j], arr[i]  #SWAP


########################## BUBBLE SORT FUNCTION ##################################
def bubble_sort(arr):
    n=len(arr)
    for i in range(n-1):
            for j in range(0, n-i-1):
                if (arr[j] > arr[j + 1]):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]  

########################## SORTING FUNCTION FOR EACH ALGORITHM #######################
def sort():
    arr=[]
    k=arr_name.get()
    for i in range(k):  
        arr.append(np.random.randint(k))
    n = len(arr)

    ############### Merge Sort ###################
    if algo_comboBox.get()=='Merge Sort':
        start=time.time()
        print(start)
        merge_sort(arr, 0, len(arr)-1)
        stop=time.time()
        print(stop)
        time_string= stop-start
        print(time_string)
        result.config(text=time_string)
    
    ############### Heap Sort ###################
    if algo_comboBox.get()=='Heap Sort':
        start=time.time()
        print(start)
        heap_sort(arr)
        stop=time.time()
        print(stop)
        time_string= stop-start
        print(time_string)
        result.config(text=time_string)

    ############# Quick Sort #####################
    elif algo_comboBox.get()=='Quick Sort':
        start=time.time()
        print(start)
        quick_sort(arr,0,len(arr)-1)
        stop=time.time()
        print(stop)
        time_string= stop-start
        print(time_string)
        result.config(text=time_string)

    ############# Quick Sort 3 Medians #####################
    elif algo_comboBox.get()=='Quick Sort 3 Medians':
        start=time.time()
        print(start)
        quicksort_median(arr)
        stop=time.time()
        print(stop)
        time_string= stop-start
        print(time_string)
        result.config(text=time_string)
    
    ############# InsertionSort #####################
    elif algo_comboBox.get()=='Insertion Sort':
        start=time.time()
        insertion_sort(arr)
        stop=time.time()
        time_string= stop-start
        result.config(text=time_string)

    ############# Selection Sort #####################
    elif algo_comboBox.get()=='Selection Sort':
        start=time.time()
        selection_sort(arr)
        stop=time.time()
        time_string= stop-start
        result.config(text=time_string)
                     
    
    ############# Bubble Sort #####################
    elif algo_comboBox.get()=='Bubble Sort':
        start=time.time()
        bubble_sort(arr)
        stop=time.time()
        time_string= stop-start
        result.config(text=time_string)

########################## FRAME TO DISPLAY CONTENTS ################################
display_window = Frame(root, width= 900, height=1300, bg="white")
display_window.grid(row=1, column=5, padx=400, pady=150 ,ipadx=50,ipady=50)


lbl1 = Label(display_window, text=" Choose Algorithm: ", bg="white")
lbl1.grid(row=0, column=0, padx=10, pady=15, sticky=W)
algo_comboBox = ttk.Combobox(display_window, textvariable=algorithms, values=list)
algo_comboBox.grid(row=0, column=1, padx=5, pady=5)
algo_comboBox.current(0)

arr_name=IntVar()

lbl2 = Label(display_window, text="Array Length: ", bg="white")
lbl2.grid(row=1, column=0, padx=10, pady=15, sticky=W)
length_comboBox = ttk.Entry(display_window, textvariable=arr_name)
length_comboBox.grid(row=1, column=1, padx=5, pady=5)


def myfunction():
    print(arr_name.get())

###################### BUTTONS USING TKINTER #############################
btn1 = Button(display_window, text="Show Array Size", command=myfunction, bg="blue",fg="white" )
btn1.grid(row=4, column=0, padx=5, pady=15)

btn2 = Button(display_window, text="Show Array", command=createArr, bg="orange")
btn2.grid(row=4, column=1, padx=5, pady=15)

btn3 = Button(display_window, text="Sort", command=sort, bg="yellow")
btn3.grid(row=4, column=2, padx=5, pady=15)


btn4 = Button(display_window, text="Compare", command=compare, bg="#00FF00")
btn4.grid(row=4, column=3, padx=5, pady=15)

result=Label(display_window,text="Your Result")
result.grid(row=6,column=0,padx=15, pady=15)




root.mainloop()
