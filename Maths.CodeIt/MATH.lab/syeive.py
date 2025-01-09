n = int(input())
prime = [True] * (n + 1)
p = 2
while p * p <= n:
    if prime[p] == True:
        for  i in range(2,n+1,p):
            prime[i] = False
    p += 1
primes = [p for p in prime if prime[p] == True]
print(prime)