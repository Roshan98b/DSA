from math import sqrt

def factors(N):
    factor = {1,N}
    i = 2
    l = sqrt(N)+1
    while i < l:
        if N%i == 0:
            factor.add(i)
            factor.add(int(N/i))
        i += 1
    return len(factor)

def Div(q, arr):
    memo = {}
    result = []
    for i in range(q):
        div3_sum = 0
        for i in range(4,arr[i]):
            factor = 0
            if i in memo:
                factor = memo[i]
            else:
                factor = factors(i)
                memo[i] = factor
            if factor == 3:
                div3_sum += 1
        result.append(div3_sum)
    return result

if __name__ == "__main__":
    q = 2
    arr = [6,10]
    print (Div(q, arr))