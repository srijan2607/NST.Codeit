n = int(input())
# for i in range(1,n+1) : # No of Row to print
#     for j in range(1,n+1): # No of Column to print
#         print("*", end=" ")
#     print()
k = 1
for i in range(1, n+1 ): 
    for j in range(1, k + 1):
        print("*", end=" ")
    k += 2
    print()


