n = int(input())
sol = 0
for i in range(n):
    p,v,t = map(int,input().split())
    if (p+v+t >= 2) :
        sol += 1
print(sol)