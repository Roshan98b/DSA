def count_sum(target_sum, numbers, memo={}):
    if(target_sum in memo):
        return memo[target_sum]
    elif(target_sum == 0):
        return 1
    elif(target_sum < 0):
        return 0
    else:
        count = 0
        for num in numbers:
            count += count_sum(target_sum - num, numbers, memo)
            memo[target_sum] = count
        return count


if __name__ == "__main__":
    target_sum = 7
    numbers = [1]
    print(count_sum(target_sum, numbers))
