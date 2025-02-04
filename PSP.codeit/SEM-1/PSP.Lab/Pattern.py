n = int(input("Enter your No."))
for row in range(1, (n+1)):
    for j in range(row):
        print("*", end = " ")
    print()
for row in range(n-1 , 0 , -1): # -1 bcs it will dec the number in the -ve direction
    for j in range(row):
        print("*", end = " ")
    print()