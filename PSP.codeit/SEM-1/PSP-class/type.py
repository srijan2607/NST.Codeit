# a = 5
# b = 6.78
# c = "Ram"
# d = 'a'

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))

"""Given two numbers, N1 and N2, perform the following sequence of operations to calculate the final result:

1. Add N1 and N2 and store the result in a variable called result_1. 
2. Multiply result_1 by 5 and update the value in result_1. 
3. Divide result_1 by 2 and update the value in result_1. 
4. Subtract the sum of the original two numbers, N1 and N2, from result_1, and update the value in result_1. 
6. Raise result_1 to the power of 2 and update the value in result_1. 
7. Take the modulo of result_1 with 5 and update the value in result_1. Print the final value of result_"""

N1 = int(input())
N2 = int(input())

result_1 = N1 + N2
result_1 *= 5
result_1 /= 2
result_1 -= N1 + N2
result_1 **= 2
result_1 %= 5
print(result_1)

'''Write a program that checks if a person is eligible to vote based on their age and citizenship status.
The program takes an integer age representing the person's age and a string is_citizen ('Y' for Yes, 'N' for No) representing their citizenship status, as input, and prints whether the person is eligible to vote or not.'''



age = int(input())
citizen = input()

if citizen == 'Y' and age >= 18:
    print("You are eligible to vote.")
else :
    print("You are not eligible to vote.")

'''Temp < 0 : Freezing Weather
Temp 0-9 : Very Cold
Temp 10-19 : Cold
Temp 20-29 : Normal
Temp 30-39 :  Hot
Temp >=40 : Very Hot'''


# Temp = int(input())
# if Temp < 0 :
#     print("Freezing Weather")
# elif Temp > 0 and Temp <= 9 :
#     print("Cold Weather")
# elif Temp > 9 and Temp <= 19 :
#     print("Cool Weather")
# elif Temp > 19 and Temp <= 29 :
#     print("Normal")
# elif Temp > 29 and Temp <= 39 :
#     print("Hot")
# elif Temp >= 40 :
#     print("Very Hot")   

'''Find the minimum and maximum digit present in the number as given by the user.

User Task:
This is a function problem. You don't have to take any input. You are required to complete the function min_max_digits() that takes an integer n as parameter and returns the minimum and maximum digits from the given integer n.'''

def min_max_digits(n):
    ld = []  # List to store the digits
    
    # Extract digits from the number
    while n != 0:
        digit = n % 10  # Get the last digit
        n = n // 10     # Remove the last digit from the number
        ld.append(digit)  # Append the digit to the list
    
    # Return the minimum and maximum digits
    return min(ld), max(ld)

print(min_max_digits())
