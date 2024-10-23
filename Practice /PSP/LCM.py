def LCM(a, b):
    g_n = max(a,b)
    for num in range(g_n, (a*b)+1):
        if num%a == 0 and num%b == 0:
            return num
