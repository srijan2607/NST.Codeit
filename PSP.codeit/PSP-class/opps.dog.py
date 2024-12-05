# class dog:
#     def __init__(self, name, age, breed):
#         self.name = name
#         self.age = age
#         self.breed = breed
#     def eat(self):
#         print(self.name, " is eating....")
#     def sleep(self):
#         print(self.name, "is sleeping....")
#     def bark(self):
#         print(self.name, "is barking....")
#     def walk(self):
#         print("The dog is walking....")
# tommy = dog("Tommy", 3, "German Shepherd")
# shenu = dog("Shenu", 4, "Pomeranian")
# shenu.eat()
# tommy.sleep()
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

#     def perimeter(self):
#         return 2 * (self.length + self.width)

# l,b = map(int,input().split())
# r1 = (Rectangle(l,b))
# print(r1.perimeter()) 
# print(r1.area())
 
# ____________________________________________________________________________________

# class Employee:
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def annual_salary(self):
#         return (12 * self.salary)
    
# nm = input()
# sal = int(input())
# emp = Employee(nm,sal)
# print(emp.annual_salary())

class Counter:
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
    
    def get_count(self):
        return self.count

counter = Counter()
counter.increment()
counter.increment()
print(counter.get_count())
