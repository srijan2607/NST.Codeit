#     def __init__(self, name, author, pages):
#         self.name = name
#         self.author = author
#         self.pages = pages
# x = input()
# y = input()
# z= int(input())
# book1 = book(x,y,z)

# class Car:
#     def __init__(self, make):
#         self.make = make
#     def display_info(make):
#         return f"The car make is {make}"

# car = Car("Toyota")
# print(car.display_info())

class Car:
    make = "Toyota"
    model = "Corolla"

car = Car()
print(car.make)