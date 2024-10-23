def print_perfect_numbers(a, b):
    sum1 = 0
    for n in range(a,b):
        for i in range(a,b):
            if(n % i == 0):
                sum1 = sum1 + i
            if (sum1 == n):
                print(i)
        print()