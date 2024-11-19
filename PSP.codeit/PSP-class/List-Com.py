# ls = [x for x in range(1,101) if  x % 3 == 0]
# print(ls)

# ls =  [x for x in range(2,12) if  x % 2 != 0]
# print(ls)

# L = [[1,2,3], [4,5,6], [7,8,9]]
# for i in L :
#     for j in i :
#         print(j , end = " ")
#     print()

L = [[1,2,3], [4,5,6], [7,8,9]]
r = len(L)
c = len(L[0])
for i in range(r):
    for j in range(c):
        print(L[i],[j], end = " ")
        