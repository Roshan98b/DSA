def selection_sort(arr):
    pos = 0
    N = len(arr)
    for i in range(N):
        pos = i
        for j in range(i+1,N):
            if arr[i] > arr[j]:
                pos = j
        temp = arr[i]
        arr[i] = arr[pos]
        arr[pos] = temp
