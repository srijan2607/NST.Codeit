# import math

# def is_prime(n):
#     if n <2 : 
#         return False
#     k = math.sqrt(n)
#     for i in range(2,int(k) + 1):
#        if n % i == 0 :
#            return False
#     return True

def Area(side):
    cal = (3.14) * (side**2)
    return round(cal, 2)

#don't change anything below this line
side = int(input())
print(Area(side))