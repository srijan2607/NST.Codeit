# # Global variables
# x = 10
# def print_local_and_global_variable() :
#     # Local variable
#     global x 
#     x = 5
#     print("Local variable x : ", x)

# print_local_and_global_variable()
# print("Global variable x : ", x)



a = int(input())
b = int(input())

def add(a,b) :
    return a+b
def subtract(a,b) :
    return a - b
def multiply(a,b) :
    return a*b
def divide(a,b) :
    if b == 0 :
        return "Error: Division by zero"
    else :
        return a/b
def remainder(a,b) :
    return a % b

print("Addition : ", add(a,b))
print("Subtraction : ", subtract(a,b))
print("Multiplication : ", multiply(a,b))
print("Division : ", divide(a,b))
print("Remainder : ", remainder(a,b))


