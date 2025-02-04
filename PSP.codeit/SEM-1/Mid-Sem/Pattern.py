# n = int(input())
# for i in range(1,n+1): # Tell us the height of the Triangle # n is fixed and tells us how many rows to print, while i varies with each row to determine how many stars to print on that particular row.
#     for j in range(1, 1+i): #   Tell us the Length of the Triangle # i design allows the triangle to grow in height and width appropriately, creating a visually appealing right-angled triangle.
#         print("*", end = " ")
#     print()


# n = int(input())
# k = 1
# for i in range(1, n+1 ): 
#     for j in range(1, k + 1):
#         print("*", end=" ")
#     k += 2
#     print()


# n = int(input())
# for i in range(n):
#     for j in range(n-i-1):
#         print(end= " ")
#     for j in range(2*i + 1):
#         print("*", end= "")
#     print()

# n = int(input())
# for i in range(n, 0, -1):
#     for j in range(0,n-i):
#         print(end= " ")
#     for j in range(0,):
#         print("*", end= "")
#     print()

# n = int(input())
# for i in range(n):
#     for j in range(1, n - i - 1):
#         print(" ",end= " ")
#     for j in range(n):
#         print("*", end= "")
#     print()

# n = int(input())
# for i in range(1,n+1):
#     for j in range(i):
#         print("*", end=" ")
#     for j in range(n-i-1):
#         print(" ", end=" ")
#     print()

# n = int(input())
# for i in range(n,0,-1): # to start the range form n
#     for j in range(i,n+1): # Ex:- 1st the i will be = 5 and n+1 = 6 and so on... 4 and 6 => 45 will be printed
#         print(j, end = "")
#     print()