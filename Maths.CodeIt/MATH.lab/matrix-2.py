# row1 , col1 = map(int,input().split())
# matrix1 = []
# for i in range(row1):
#     temp1 = list(map(int, input().split()))
#     matrix1.append(temp1)

# row2 , col2 = map(int,input().split())
# matrix2 = []
# for i in range(row2):
#     temp2 = list(map(int, input().split()))
#     matrix2.append(temp2)

# if col1 != row2:
#     print("Matrix Addition is not possible")
# else:
#     for i in range(row1):
#         for j in range(col2):
#             print(matrix1[i][j] + matrix2[i][j], end = " ")
#         print()

row1 , col1 = map(int,input().split())
matrix1 = []
for i in range(row1):
    temp1 = list(map(int, input().split()))
    matrix1.append(temp1)

row2 , col2 = map(int,input().split())
matrix2 = []
for i in range(row2):
    temp2 = list(map(int, input().split()))
    matrix2.append(temp2)

