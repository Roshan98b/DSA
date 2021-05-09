def can_sum(target_sum, numbers):
    arr = [False for i in range(target_sum+1)]
    arr[0] = True
    for i in range(target_sum+1):
        if arr[i] == True:
            for number in numbers:
                if i + number < target_sum + 1:
                    arr[i + number] = True
    return arr[target_sum]


if __name__ == "__main__":
    target_sum = 7
    numbers = [5, 3, 4]
    print(can_sum(target_sum, numbers))
