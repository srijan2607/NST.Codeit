# a = int(input())
# b = int(input())

# def add(a,b) :
#     return a+b
# def subtract(a,b) :
#     return a - b
# def multiply(a,b) :
#     return a*b
# def divide(a,b) :
#     if b == 0 :
#         return "Error: Division by zero"
#     else :
#         return a/b
# def remainder(a,b) :
#     return a % b

# print("Addition : ", add(a,b))
# print("Subtraction : ", subtract(a,b))
# print("Multiplication : ", multiply(a,b))
# print("Division : ", divide(a,b))
# print("Remainder : ", remainder(a,b))
"""---------------------------------------------------------------------------------------"""
''''
calculate_item_value(): Takes two numbers price and quantity as 
input from the user and returns the total value for a given item 
based on the numbers.

calculate_total_inventory_value(): Uses another function 
calculate_item_value() to calculate individual item value, 
and then calculates the total inventory value.

Note:- There are three items in the inventory'''

# price, quantity = list(int(input())).split()

# def calculate_item_value(price, quantity):
#     return price * quantity
# def calculate_total_inventory_value() :
#     item_1_value = calculate_item_value(price, quantity)
#     item_2_value = calculate_item_value(price, quantity)
#     item_3_value = calculate_item_value(price, quantity)
#     return item_1_value + item_2_value + item_3_value

# print("Total inventory value:", calculate_total_inventory_value())

"""----------------------------------------------------------------"""


num = 10 
def check_scope():
    num2  = 10 + num 
    num = 5 
    print(num2)
check_scope()