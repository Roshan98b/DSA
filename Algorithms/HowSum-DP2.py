def how_sum(target_sum, numbers):
    arr = [None for i in range(target_sum + 1)]
    arr[0] = [[]]
    for index in range(target_sum + 1):
        if(arr[index] != None):
            for number in numbers:
                if(index+number <= target_sum):
                    if arr[index+number] == None:
                        arr[index+number] = [[number]]
                    else:
                        flag = True
                        for indexj, ways in enumerate(arr[index+number]):
                            if number in ways:
                                flag = False
                                arr[index+number][indexj].append(number)
                        if flag:
                            arr[index+number].append([number])
    return arr[target_sum]


if __name__ == "__main__":
    target_sum = 7
    numbers = [5, 3, 4, 2]
    print(how_sum(target_sum, numbers))
