# 1. Vehicle → Car
# Vehicle: brand, speed. Car: fuel_type. Use super(). Display all.
class Vehicle:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
class car(Vehicle):
    def __init__(self,brand,speed,fuel_type):
        super().__init__(brand,speed)
        self.fuel_type=fuel_type

    def display(self):
        print(self.brand,self.speed,self.fuel_type)
c=car("toyota",120,"petrol")
c.display()      

# 2. Person → Teacher
# Person: name, age. Teacher: subject. Use super(). Display all.
class Teacher:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class person(Teacher):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject=subject

    def display(self):
        print(self.name,self.age,self.subject)
c=car("sneha",20,"python")
c.display()      

# 3. Employee → Manager
# Employee: emp_id, salary. Manager: department. Use super().
class employee:
    def __init__(self,emp_id,salary):
        self.emp_id=emp_id
        self.salary=salary
class manager(employee):
    def __init__(self,emp_id,salary,department):
        super().__init__(emp_id,salary)
        self.department=department

    def display(self):
        print(self.emp_id,self.salary,self.department)
c=car(101,200000,"data enginering")
c.display()     

# 4. Product → Electronics
class Product:
    def _init_(self, name, price):
        self.name = name
        self.price = price

class Electronics(Product):
    def _init_(self, name, price, warranty_years):
        super()._init_(name, price)
        self.warranty_years = warranty_years

    def display(self):
        print(self.name, self.price, self.warranty_years)

e = Electronics("TV", 30000, 2)
e.display()

# 5. Animal → Dog
class Animal:
    def _init_(self, name, species):
        self.name = name
        self.species = species

class Dog(Animal):
    def _init_(self, name, species, breed):
        super()._init_(name, species)
        self.breed = breed

    def display(self):
        print(self.name, self.species, self.breed)

d = Dog("Tommy", "Mammal", "Labrador")
d.display()

# 6. Account → SavingsAccount
class Account:
    def _init_(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

class SavingsAccount(Account):
    def _init_(self, account_number, balance, interest_rate):
        super()._init_(account_number, balance)
        self.interest_rate = interest_rate

    def display(self):
        print(self.account_number, self.balance, self.interest_rate)

a = SavingsAccount(12345, 10000, 5)
a.display()

# 7. User → Admin
class User:
    def _init_(self, username, email):
        self.username = username
        self.email = email

class Admin(User):
    def _init_(self, username, email, permissions):
        super()._init_(username, email)
        self.permissions = permissions

    def display(self):
        print(self.username, self.email, self.permissions)

ad = Admin("admin1", "admin@mail.com", "All Access")
ad.display()

# 8. Book → Ebook
class Book:
    def _init_(self, title, author):
        self.title = title
        self.author = author

class Ebook(Book):
    def _init_(self, title, author, file_size):
        super()._init_(title, author)
        self.file_size = file_size

    def display(self):
        print(self.title, self.author, self.file_size)

b = Ebook("Python", "ABC", "5MB")
b.display()

# 9. Appliance → WashingMachine
class Appliance:
    def _init_(self, brand, power):
        self.brand = brand
        self.power = power

class WashingMachine(Appliance):
    def _init_(self, brand, power, capacity):
        super()._init_(brand, power)
        self.capacity = capacity

    def display(self):
        print(self.brand, self.power, self.capacity)

w = WashingMachine("LG", "500W", "7kg")
w.display()

# 10. Shape → Circle
class Shape:
    def _init_(self, color):
        self.color = color

class Circle(Shape):
    def _init_(self, color, radius):
        super()._init_(color)
        self.radius = radius

    def display(self):
        print(self.color, self.radius)

s = Circle("Red", 5)
s.display()

# 11 Device → Laptop
class Device:
    def _init_(self, name, price):
        self.name = name
        self.price = price

class Laptop(Device):
    def _init_(self, name, price, ram):
        super()._init_(name, price)
        self.ram = ram

    def display(self):
        print(self.name, self.price, self.ram)

l = Laptop("HP", 60000, "8GB")
l.display()

# 12. Food → Fruit
class Food:
    def _init_(self, name, calories):
        self.name = name
        self.calories = calories

class Fruit(Food):
    def _init_(self, name, calories, vitamin_content):
        super()._init_(name, calories)
        self.vitamin_content = vitamin_content

    def display(self):
        print(self.name, self.calories, self.vitamin_content)

f = Fruit("Apple", 95, "Vitamin C")
f.display()

# 13. Company → Startup
class Company:
    def _init_(self, name, location):
        self.name = name
        self.location = location

class Startup(Company):
    def _init_(self, name, location, funding_amount):
        super()._init_(name, location)
        self.funding_amount = funding_amount

    def display(self):
        print(self.name, self.location, self.funding_amount)

s = Startup("TechX", "Delhi", "5 Crore")
s.display()

# 14. Student → GraduateStudent
class Student:
    def _init_(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

class GraduateStudent(Student):
    def _init_(self, name, roll_no, degree):
        super()._init_(name, roll_no)
        self.degree = degree

    def display(self):
        print(self.name, self.roll_no, self.degree)

g = GraduateStudent("Sneha", 101, "MCA")
g.display()

# 15. Bank → Branch
class Bank:
    def _init_(self, name, city):
        self.name = name
        self.city = city

class Branch(Bank):
    def _init_(self, name, city, branch_code):
        super()._init_(name, city)
        self.branch_code = branch_code

    def display(self):
        print(self.name, self.city, self.branch_code)

b = Branch("SBI", "Jaipur", 1234)
b.display()

# 16. Course → OnlineCourse
class Course:
    def _init_(self, course_name, duration):
        self.course_name = course_name
        self.duration = duration

class OnlineCourse(Course):
    def _init_(self, course_name, duration, platform):
        super()._init_(course_name, duration)
        self.platform = platform

    def display(self):
        print(self.course_name, self.duration, self.platform)

c = OnlineCourse("Python", "3 Months", "Udemy")
c.display()

# 17. Employee → Developer
class Employee:
    def _init_(self, name, salary):
        self.name = name
        self.salary = salary

class Developer(Employee):
    def _init_(self, name, salary, programming_language):
        super()._init_(name, salary)
        self.programming_language = programming_language

    def display(self):
        print(self.name, self.salary, self.programming_language)

d = Developer("Rahul", 70000, "Python")
d.display()

# 18. Vehicle → Bike
class Vehicle:
    def _init_(self, brand, speed):
        self.brand = brand
        self.speed = speed

class Bike(Vehicle):
    def _init_(self, brand, speed, mileage):
        super()._init_(brand, speed)
        self.mileage = mileage

    def display(self):
        print(self.brand, self.speed, self.mileage)

b = Bike("Honda", 100, "50km/l")
b.display()

# 19. Person → Employee
class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def _init_(self, name, age, job_role):
        super()._init_(name, age)
        self.job_role = job_role

    def display(self):
        print(self.name, self.age, self.job_role)

e = Employee("Amit", 25, "Engineer")
e.display()

# 20. Shape → Rectangle
class Shape:
    def _init_(self, color):
        self.color = color

class Rectangle(Shape):
    def _init_(self, color, length, width):
        super()._init_(color)
        self.length = length
        self.width = width

    def display(self):
        print(self.color, self.length, self.width)

r = Rectangle("Blue", 10, 5)
r.display()