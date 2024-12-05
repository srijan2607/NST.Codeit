# Your code 
n = int(input())
tt = 0
fact = 1
fact2 = 1
if n % 2 != 0 :
    print(0)
for i in range(n+1):
    fact *= n
    print()
for j in range(n/2):
    fact2 *= n/2
    print()
facto = int(fact/(fact2*fact2))
