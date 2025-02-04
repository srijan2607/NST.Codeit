n = int(input())
if n == 0: 
    print(1)
else: 
    carry = 0
    result = 0 
    place = 1
    temp = n
    while n :
        dig = n % 10 
        sum += dig + carry+ 1
        if sum >= 10 :
            carry = 1
            sum_ = sum % 10 
        else :
            carry = 0
        result += sum * place
        place = place * 10
        n = n // 10
    print(result+ carry * place)