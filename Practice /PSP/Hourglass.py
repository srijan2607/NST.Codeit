row = int(input())
for i in range(row, 0, -1):
    for j in range(row-i):
        print(" ", end=" ")
    for j in range(1, 2*i):
        if i==1 or i==row or j==1 or j==2*i-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
for i in range(2, row+1):
    for j in range(row-i):
        print(" ", end=" ")
    for j in range(1, 2*i):
        if i==row or j==1 or j==2*i-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()