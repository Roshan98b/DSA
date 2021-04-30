def factors(N):
    sums = 1
    limit = N//2
    for i in range(2,limit+1):
        if N%i == 0:
            sums += i
    return sums

def perfect_number(N):
    if (factors(N) == N):
        return True
    else:
        return False

if __name__ == "__main__":
    N = 10000000000
    print(perfect_number(N))