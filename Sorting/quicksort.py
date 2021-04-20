def _partition(arr, N):
    if (N < 1):
        return []
    pivot = arr[N-1]
    i=0
    j=N-1
    while (i < j):
        while (arr[i] < pivot):
            i += 1
        while (arr[j] > pivot):
            j -= 1
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    
    left = _partition(arr[:i], len(arr[:i]))
    right = _partition(arr[i+1:], len(arr[i+1:]))

    # Using the list by reference 
    arr[:] = left + [pivot] + right
    return arr

def quick_sort(arr):
    N = len(arr)
    _partition(arr, N)

