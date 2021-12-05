def partition(arr, low, high, drawArray):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot
 
    drawArray(arr)
    for j in range(low, high):
        if arr[j] <= pivot:
 
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quickSort(arr, low, high, drawArray):
    if len(arr) == 1:
        return arr
    # time.sleep(0.02)
    if low < high:
        pi = partition(arr, low, high, drawArray)
        quickSort(arr, low, pi-1, drawArray)
        quickSort(arr, pi+1, high, drawArray)

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
def mergeSort(arr, l, r, drawArray):
    drawArray(arr)
    if l < r:
        m = l+(r-l)//2
 
        mergeSort(arr, l, m, drawArray)
        mergeSort(arr, m+1, r, drawArray)
        merge(arr, l, m, r)

def bubbleSort(array, drawArray):
    haveDoneSwitch = True
    while haveDoneSwitch:
        haveDoneSwitch = False
        drawArray(array)
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                haveDoneSwitch = True
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp
                # time.sleep(0.05)

def heapify(arr, n, i):
    largest = i  
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr, n, largest)
def heapSort(arr, drawArray):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        drawArray(arr)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
        drawArray(arr)

def insertionSort(arr, drawArray):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        drawArray(arr)
        while j >=0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

def selectionSort(lst, drawArray):
    n = len(lst)
    for i in range(n - 1):
        drawArray(lst)
        min = i
        for j in range(i + 1, n):
            if(lst[j] < lst[min]):
                min = j
        lst[i], lst[min] = lst[min], lst[i]

def shellSort(arr, drawArray):
    n = len(arr)
    gap = int(n/2)
    while gap > 0:
        for i in range(gap,n):
            if i % 10==0:
                drawArray(arr)
            temp = arr[i]
            j = i
            while  j >= gap and arr[j-gap] >temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        gap //= 2

def getNextGap(gap):
  
    # Shrink gap by Shrink factor
    gap = int((gap * 10)/13)
    if gap < 1:
        return 1
    return gap

def combSort(arr, drawArray):
    n = len(arr)
  
    # Initialize gap
    gap = n
  
    # Initialize swapped as true to make sure that
    # loop runs
    swapped = True
  
    # Keep running while gap is more than 1 and last
    # iteration caused a swap
    while gap !=1 or swapped == 1:
  
        # Find next gap
        gap = getNextGap(gap)
  
        # Initialize swapped as false so that we can
        # check if swap happened or not
        swapped = False
  
        # Compare all elements with current gap
        for i in range(0, n-gap):
            if i%10 == 0:
                drawArray(arr)
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap]=arr[i + gap], arr[i]
                swapped = True




# Python3 program to
# sort array using
# pancake sort
 
# Reverses arr[0..i] */
def flip(arr, i):
    start = 0
    while start < i:
        temp = arr[start]
        arr[start] = arr[i]
        arr[i] = temp
        start += 1
        i -= 1
 
# Returns index of the maximum
# element in arr[0..n-1] */
def findMax(arr, n, drawArray):
    mi = 0
    for i in range(0,n):
        if arr[i] > arr[mi]:
            mi = i
    return mi
 
# The main function that
# sorts given array
# using flip operations
def pancakeSort(arr, n, drawArray):
     
    # Start from the complete
    # array and one by one
    # reduce current size
    # by one
    curr_size = n
    while curr_size > 1:
        # Find index of the maximum
        # element in
        # arr[0..curr_size-1]
        mi = findMax(arr, curr_size, drawArray)
 
        # Move the maximum element
        # to end of current array
        # if it's not already at
        # the end
        if mi != curr_size-1:
            # To move at the end,
            # first move maximum
            # number to beginning
            flip(arr, mi)
 
            # Now move the maximum
            # number to end by
            # reversing current array
            flip(arr, curr_size-1)
            drawArray(arr)
        curr_size -= 1

def bucketSort(array, drawArray):
    m = max(array)
    for i in range(len(array)):
        array[i] /= m
    bucket = []

    # Create empty buckets
    for i in range(len(array)):
        bucket.append([])

    # Insert elements into their respective buckets
    for j in array:
        index_b = int(10 * j)
        bucket[index_b].append(j)

    # Sort the elements of each bucket
    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])

    # Get the sorted elements
    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            drawArray(array)
            array[k] = bucket[i][j]
            k += 1
    return array

def compare_swap(a, i, j, d):
    if (d == 1 and a[i] > a[j]) or (d == 0 and a[i] < a[j]):
        a[i], a[j] = a[j], a[i]
  
 
def merge2(a, l, cnt, d, drawArray):
    if cnt > 1:
        k = int(cnt / 2)
        drawArray(a)
        for i in range(l, l + k):
            compare_swap(a, i, i + k, d)
        merge2(a, l, k, d, drawArray)
        merge2(a, l + k, k, d, drawArray)
 
def bitonicSort(a, l, cnt, d, drawArray):
    if cnt > 1:
        drawArray(a)
        k = int(cnt / 2)
        bitonicSort(a, l, k, 1, drawArray)
        bitonicSort(a, l + k, k, 0, drawArray)
        merge2(a, l, cnt, d, drawArray)