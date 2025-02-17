# tower of hanoi 

def tower(n):
    if n == 0:
        return 0
    return 2 * tower(n-1) + 1
n = 5
print(tower(n))
