def count_sum(target_sum, numbers):
    arr = [0 for i in range(target_sum+1)]
    arr[0] = 1
    for index in range(target_sum+1):
        if(arr[index] != 0):
            for number in numbers:
                if(index+number <= target_sum):
                    arr[index+number] += arr[index]
    return arr[target_sum]


if __name__ == "__main__":
    target_sum = 7
    numbers = [5, 3, 4]
    print(count_sum(target_sum, numbers))
