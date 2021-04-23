def can_sum(target_sum, numbers, sums = 0, sum_numbers = [], memo = {}):
    if sums == target_sum:
        return True
    elif sums > target_sum:
        return False
    elif str(sum_numbers) in memo:
        return memo[str(sum_numbers)]
    else: 
        sums = sum(sum_numbers)
        memo[str(sum_numbers)] = sums
        res = []
        for i in numbers:
            res.append(can_sum(target_sum, numbers, sums, sum_numbers + [i], memo))
        if True in res:
            return True
        else:
            return False

if __name__ == "__main__":

    target_sum = 7
    numbers = [3,4]

    print (can_sum(target_sum, numbers))

