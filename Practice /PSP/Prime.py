def print_primes_in_range(A, B):
    for num in range(A,B+1):
        is_primes = True
        if num <= 1:
            is_primes = False
        for div in range(2, num):
            if (num % div) == 0:
                is_primes = False
                break
        if is_primes == True :
            print(num, end = " ")