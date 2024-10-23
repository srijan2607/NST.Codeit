# num_1 = int(input())
# num_2 = int(input())
# num_3 = int(input())

# if num_1 == num_2 == num_3 :
#     print("Equilateral triangle")
# elif num_1 == num_2 or num_1 == num_3 or num_2 == num_3 :
#     print("Isosceles triangle")
# elif num_1 != num_2 and num_1 != num_3 and num_2 != num_3 :
#     print("Scalene triangle")


# num_1 = int(input())
# if num_1 % 4 == 0 and (num_1 % 400 == 0 or num_1 % 100 == 0) :
#     print(num_1,"is a leap year")
# else:
#     print(num_1,"is not a leap year")

side1 = int(input())
side2 = int(input())
side3 = int(input())

if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
    print("Triangle is valid.")
else :
    print("Triangle is not valid.")