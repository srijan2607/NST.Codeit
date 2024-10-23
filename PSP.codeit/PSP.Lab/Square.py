def check_star_dancer(n):
    n = int(input())
    d = n**0.5
    if d - int(d) == 0:
        print("You are the Star Dancer")
    else :
        print("Keep Dancing")
