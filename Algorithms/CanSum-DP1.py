def can_sum_tab(target_sum, arr, N):
    target = {}
    target[0] = True
    target[target_sum] = False
    for i in range(target_sum+1):
        count = 0
        if i in target:
            for num in arr:
                if (i+num <= target_sum):
                    count += 1 
                    target[i+num] = True
                else:
                    arr.remove(num)
    return target[target_sum]

if __name__ == "__main__":
    target_sum = 9
    arr = [1,2]
    N = len(arr)
    print (can_sum_tab(target_sum, arr, N))