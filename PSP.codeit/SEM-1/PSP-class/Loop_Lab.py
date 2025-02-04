# for i in range(10):
#     if i == 2 :
#         pass
#     print(i)


# def sum_of_evens_in_range():
#     a = int(input())
#     b = int(input())
#     tt = 0
#     for i in range(a,b+1):
#         if i % 2 == 0 :
#             tt += i
#     return tt
# print(sum_of_evens_in_range())

# def isPalindrome(N) :
#     temp = N
#     reverse = 0
#     while temp != 0 :
#         digit = temp % 10
#         reverse = reverse * 10 + digit
#         temp = temp // 10
#     if reverse == N :
#         return True
#     else :
#         return False

def is_prime(n):
    if n <2 : 
        return False
    for i in range(2,n):
       if n % i == 0 :
           return False
    return True