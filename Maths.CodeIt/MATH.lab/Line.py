x1 , y1 = map(int,input().split())
x2 , y2 = map(int,input().split())
x3 , y3 = map(int,input().split())

if ((y2 - y1)/(x2 - x1) == (y3 - y2) / (x3 - x2)) :
     print("yes")
else:
    print("No")

