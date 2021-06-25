def how_sum(target_sum, numbers, memo = {}):
    if(target_sum in memo):
        return memo[target_sum]
    elif(target_sum == 0):
        return []
    elif(target_sum<0):
        return None
    else: 
        result = []
        for number in numbers:
            new_number = target_sum - number
            result = how_sum(new_number, numbers, memo)
            if(result != None):
                result.append(number)
                memo[target_sum] = result
                return memo[target_sum]
           
    return None 

print(how_sum(7,[5,4,3]))
            
