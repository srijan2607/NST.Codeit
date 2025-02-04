# for counter in [1, 2, 3, 4] :
#     print("Srijan")

# for i in range(0,1001) :
#     print("Srijan")

# for i in range(0,9) :
#     print(i)

# for i in range(1,101,2) :
#     print(i)
# n = 7 
# for i in range(1,11) :
#     print(n,"X",i,"=",n*1)

# N = int(input("Enter the No. "))
# total = 0
# for i in range(1,N) :
#     total = total + i
# print(total)


# def factorial(n):
#     for i in range(1,n+1) :
#         total = total * i
#     return total
# def print_multiplication_table(number):
#     for i in range(0,11):
#         print(number, "X", i, "=", number * i)
n = int(input("your number"))
lim =[]
def find_factors(n):
    for i in range(1,n+1) :
        if n % i == 0 :
            lim.append(i)
            return lim
find_factors(n)