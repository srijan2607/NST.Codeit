# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# result = fact(6)
# print(result)    

def fib(n):
    if n == 0:
        return 0
    elif n == 1 :
        return 1
    else :
        return fib(n-1) + fib(n-2)
result = fib(10)
print(result)

# Remember F(5) != 5 + F(4)