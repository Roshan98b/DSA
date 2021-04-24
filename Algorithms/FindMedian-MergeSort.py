def findMedianSortedArrays(nums1, nums2):
    i, j, k = 0,0,0
    m, n = len(nums1), len(nums2)
    arr = [0 for i in range((m+n))]
    while (i < m and j < n):
        if (nums1[i] > nums2[j]):
            arr[k] = nums2[j]
            j += 1
        else:
            arr[k] = nums1[i]
            i += 1
        k += 1
    while (i < m):
        arr[k] = nums1[i]
        i += 1
        k += 1
    while (j < n):
        arr[k] = nums2[j]
        j += 1
        k += 1
    median = None
    if ((m+n) % 2):
        median = arr[((m+n) // 2)]
    else:
        median = (arr[(m+n) // 2] + arr[((m+n) // 2)-1]) / 2
    return median

if __name__ == "__main__":

    nums1 = [1,2]
    nums2 = [3,4]

    median = findMedianSortedArrays(nums1, nums2)
    print (median)
     