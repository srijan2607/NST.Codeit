name = input()
name2 = input()
n = len(name)
str = ""
for i in range(n-1, -1,-1):
    str += name[i]
if str == name2:
    print("YES")
else:
    print("NO")