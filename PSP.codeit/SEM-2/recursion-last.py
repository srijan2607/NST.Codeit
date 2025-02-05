import sys 
sys.getrecursionlimit(10**8)

def reverse_string(s):  
    if len(s) <= 1:  
        return s  
    else:
        return s[-1] + reverse_string(s[:-1]) 
    # Here we are extracting the last element of the string and adding it to the result of the recursive call of the function after removing the last element.


s = input()
print(reverse_string(s))