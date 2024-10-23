def print_primes_in_range(A, B):
    for num in range(A, B+1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num, end = " ")
