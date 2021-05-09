def can_sum(target_sum: int, numbers: list, memo: dict = {}):
    if target_sum < 0:
        return False
    elif target_sum == 0:
        return True
    if target_sum in memo:
        return memo[target_sum]
    else:
        for number in numbers:
            if can_sum(target_sum - number, numbers):
                memo[target_sum] = True
                return True
        memo[target_sum] = False
        return False


if __name__ == "__main__":
    target_sum = 9
    arr = [2, 2]
    print(can_sum(target_sum, arr))
