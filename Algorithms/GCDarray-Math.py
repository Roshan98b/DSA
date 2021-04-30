def gcd_pair(A,B):
    if B==0:
        return A
    else:
        return gcd_pair(B,A%B)

def gcd(n, arr):
    if n==1:
        return arr[0]
    A = arr[0]
    B = arr[1]
    g = gcd_pair(A,B)
    for i in range(2,n):
        g = gcd_pair(g,arr[i])
    return g


arr = [8,22,15]
n = len(arr)
print (gcd(n,arr))