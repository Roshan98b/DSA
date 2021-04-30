def kthDigit(A, B, k):
    power = A ** B
    if k>1:
        power = power // (10 ** (k-1))
    rem = power%10
    return rem

print (kthDigit(12,11,4))