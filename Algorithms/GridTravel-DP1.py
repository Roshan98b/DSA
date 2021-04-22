# No of ways to travel from top left to bottom right with blockages
def travel_count(m, n, blockage, memo = {}):
    key = str(m) + ',' + str(n)
    if (key in memo):
        return memo[key]
    elif (m == 0 or n == 0 or (m, n) in blockage):
        return 0
    elif (m == n == 1):
        return 1
    else:
        memo[key] = travel_count(m-1, n, blockage, memo) + travel_count(m, n-1, blockage, memo)
        return memo[key]

if __name__ == "__main__":

    m, n = 3, 4
    blockage = [(2,2)]
    t = travel_count(m, n, blockage)
    print (t)

