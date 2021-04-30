def quick_sort(arr, N):
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
    
    left = quick_sort(arr[:i], len(arr[:i]))
    right = quick_sort(arr[i+1:], len(arr[i+1:]))

    arr[:] = left + [pivot] + right
    return arr

def longest_subsequence(arr, N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        quick_sort(arr, N)
        print(arr, N)
        max, count = 0, 0
        for i in range(1,N):
            if arr[i]-arr[i-1] == 1:
                count += 1
            else:
                count = 0
            if max < count:
                max = count
    return max+1

if __name__ == "__main__":
    arr1 = [2,6,1,9,4,5,3]
    N1 = len(arr1)
    arr2 = [18,12,2,6,1,9,4,5,3,10,11,13,14,15,16,17,22,23,24]
    N2 = len(arr2)
    arr3 = [1]
    N3 = len(arr3)
    arr4 = [2,1]
    N4 = len(arr4)
    arr5 = [1,2]
    N5 = len(arr5)
    arr6 = []
    N6 = len(arr6)

    print (arr1)
    print (longest_subsequence(arr1, N1))
    print("")
    
    print (arr2)
    print (longest_subsequence(arr2, N2))
    print("")
    
    print (arr3)
    print (longest_subsequence(arr3, N3))
    print("")
    
    print (arr4)
    print (longest_subsequence(arr4, N4))
    print("")
    
    print (arr5)
    print (longest_subsequence(arr5, N5))
    print("")

    print (arr6)
    print (longest_subsequence(arr6, N6))
    print("")
    