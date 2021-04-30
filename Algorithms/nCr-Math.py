def fact(n):
    fact=1
    for i in range(2,n+1):
        fact *= i
    return fact

def nCr(n,r):
    num = fact(n)
    den1 = fact(n-r)
    den2 = fact(r)
    return (num // (den1 * den2)) % (10**9+7)

if __name__ == "__main__":
    n, r = 778, 116
    print (nCr(n,r))