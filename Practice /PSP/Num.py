# n = int(input())
# if n == 0 :
#     print(1)
# else:
#     carry = 0
#     result = 0 
#     temp = n
#     place = 1
#     while n :
#         dig = n%10
#         dig_sum = dig + 1 + carry
#         if dig_sum >= 10 :
#             carry = 1
#             dig_sum = dig_sum % 10 
#         else :
#             carry = 0
#         result += dig_sum * place 
#         n = n // 10
#         place = place* 10
#     print(result+ carry *place)

n = int(input())
if n == 0 :
    print(1)
else: 
    carry = 0 
    result = 0 
    temp = n
    place = 1
    while n :
        dig = n % 10
        sum = dig + carry + 1 
        if sum >= 10 :
            carry = 1
            sum = sum % 10
        else :
            carry = 0
        result += sum * place 
        n = n // 10
        place = place * 10
    print(result + carry * place)