n = int(input())
for i in range (1,n+1):
    for j in range (0,n-i):
        print(" ",end = " ")
    for j in range (0,2*i-1):
        if j == 0 or j == (2*i-2):
            print("*",end = " ")
        else:
            print(" ",end = " ")
    print()
for i in range (n-1,0,-1):
    for j in range (0,n-i):
        print(" ",end = " ")
    for j in range (0,2*i-1):
        if j == 0 or j == (2*i-2):
            print("*",end = " ")
        else:
            print(" ",end = " ")
    print()
