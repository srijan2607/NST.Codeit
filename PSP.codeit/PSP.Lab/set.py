# my_set = {1, 2, 4, 5}
# my_set.clear()
# print(my_set)
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# C = {4, 5, 6, 7}
# result = (A.intersection(B).union(C.difference(B))) - (A.symmetric_difference(C))
# print(result)
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])
C = frozenset([4, 5, 6, 7])

result = (A.union(B).difference(C)).intersection(A)
print(result)