# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         print(matrix[i][j], end = " ")
#     print()

# Input as matrix

row , col = map(int,input().split())
matrix = []
for i in range(row):
    temp = list(map(int, input().split()))
    matrix.append(temp)

print(matrix)

# for i in range(row):
#     for j in range(col):
#         print(matrix[i][j], end = " ")
#     print()
for i in matrix:
    print(*i)