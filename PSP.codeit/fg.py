# x = 100
# if x > 50:
#         print("x is greater than 50")
# if x > 150:
#         print("x is greater than 150")
# else:
#         print("x is not greater than 150")

# num = int(input())
# if num == 1 :
#     print("Monday")
# elif num == 2 :
#     print("Tuesday")
# elif num == 3 :
#     print("Wednesday")
# elif num == 4 :
#     print("Thursday")
# elif num == 5 :
#     print("Friday")
# elif num == 6 :
#     print("Saturday")
# elif num == 7 :
#     print("Sunday")
# else :
#     print("Invalid number")
# Input the number of units consumed
num = int(input("Enter the number of units consumed: "))

# Initialize total cost
total_cost = 0

# Calculate the cost based on unit slabs
if num <= 100:
    total_cost = num * 4
elif num <= 200:
    total_cost = (100 * 4) + ((num - 100) * 5)
elif num <= 300:
    total_cost = (100 * 4) + (100 * 5) + ((num - 200) * 6)
elif num <= 400:
    total_cost = (100 * 4) + (100 * 5) + (100 * 6) + ((num - 300) * 7)
else:
    total_cost = (100 * 4) + (100 * 5) + (100 * 6) + (100 * 7) + ((num - 400) * 8)

# Calculate the surcharge (10% of the total cost)
surcharge = total_cost * 0.10

# Add the surcharge to the total cost
final_bill = total_cost + surcharge

# Print the final bill amount
print("Total Electricity Bill: Rs", round(final_bill, 2))