def isTriangular(N):
    i = 1
    sum = 0
    while sum < N:
        sum = (i*(i+1))//2
        i += 1
    print (sum)
    if sum == N:
        return 1
    else:
        return 0

if __name__ == "__main__":
    N = 55
    print (isTriangular(N))