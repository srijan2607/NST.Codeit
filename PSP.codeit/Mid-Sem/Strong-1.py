def is_strong_number(n):
    original = n
    sum = 0
    fact = 1
    while n > 0:
        dig = n // 10 
        for i in range(1,dig+1):
            fact *= i
        sum += fact
        n = n % 10
    if sum == original:
        return 1
    else :
        return 0