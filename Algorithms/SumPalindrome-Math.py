def isDigitSumPalindrome(N):
    num = N
    sums = 0
    while (num != 0):
        sums += num%10
        num = num//10
    rev = 0
    num = sums
    while num != 0:
        rem = num % 10
        rev = rev*10 + rem
        num = num//10
    if rev == sums:
        return 1
    else: 
        return 0

print (isDigitSumPalindrome(56))