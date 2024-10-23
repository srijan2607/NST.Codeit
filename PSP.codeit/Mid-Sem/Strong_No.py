def find_strong_numbers_in_range(a, b):
    for num in range(a,b+1):
        original = num
        sum = 0
        fact = 1
        while num > 0:
            dig = num // 10 
            for i in range(1,dig+1):
                fact *= i
            sum += fact
            num = num % 10
        if sum == original:
            print(original)