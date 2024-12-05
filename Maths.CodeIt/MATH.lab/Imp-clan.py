x1 , y1 = map(int,input().split())
x2 , y2 = map(int,input().split())
x3 , y3 = map(int,input().split())
x4 , y4 = map(int,input().split())
x5 , y5 = map(int,input().split())

R = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
C = ((x1 - x3)**2 + (y1 - y3)**2)**0.5
M = ((x1 - x4)**2 + (y1 - y4)**2)**0.5
V = ((x1 - x5)**2 + (y1 - y5)**2)**0.5

if R is min:
    print("Chola")
elif C is min:
    print("Chandana")
elif M is min:
    print("Maratha")
else:
    print("Vijaya")
