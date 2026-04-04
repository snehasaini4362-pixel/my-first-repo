# MULTILEVEL INHERITANCE QUESTIONS

# 1. Create class Grandparent, Parent, and Child. Add methods in each and show how child
# accesses all.
class Grandparent:
    def GP(self):
        print("grandparent property")

class parent(Grandparent):
    def P(self):
        print("parent property")

class child(parent):
    def CH(self):
        print("child property")   

p1=child()
p1.GP()
p1.P()
p1.CH()             

# 2. Write a program where Animal → Mammal → Dog and each class has its own method. Call all
# methods using the Dog class.

class animal:
    def animal_display(self):
        print("animals property")

class Mammal(animal):
    def Mammal_display(self):
        print("mammal property")

class dog(Mammal):
    def dog_display(self):
        print("dog property")

cl=dog() 
cl.animal_display()
cl.Mammal_display()
cl.dog_display()       


# 3. Create a class Vehicle, then Car inherits from it, and SportsCar inherits from Car. Add methods
# at each level.
class Vehicle:
    def start(self):
        print("Vehicle starts")

class Car(Vehicle):
    def drive(self):
        print("Car drives")

class SportsCar(Car):
    def speed(self):
        print("Sports car runs fast")

s = SportsCar()
s.start()
s.drive()
s.speed()

# 4. Demonstrate constructor chaining in multilevel inheritance using super().
class A:
    def __init__(self):
        print("A constructor")

class B(A):
    def __init__(self):
        super().__init__()
        print("B constructor")

class C(B):
    def __init__(self):
        super().__init__()
        print("C constructor")

obj = C()

# 5. Create a class Shape → Rectangle → Square and calculate area at each level.
class Shape:
    def area(self):
        print("Area not defined")

class Rectangle(Shape):
    def area(self):
        l = 5
        b = 3
        print("Rectangle area =", l * b)

class Square(Rectangle):
    def area(self):
        s = 4
        print("Square area =", s * s)

sq = Square()
sq.area()

# 6. Write a program showing method overriding in multilevel inheritance.

class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(B):
    def show(self):
        print("Class C")

obj = C()
obj.show()   

# 7. Create a class Student → GraduateStudent → PhDStudent and add attributes progressively.
class Student:
    def __init__(self, name):
        self.name = name

class GraduateStudent(Student):
    def __init__(self, name, degree):
        super().__init__(name)
        self.degree = degree

class PhDStudent(GraduateStudent):
    def __init__(self, name, degree, topic):
        super().__init__(name, degree)
        self.topic = topic

    def show(self):
        print(self.name, self.degree, self.topic)

p = PhDStudent("Sneha", "MSc", "AI")
p.show()

# 8. Implement a banking system: Account → SavingsAccount → FixedDepositAccount.
class Account:
    def info(self):
        print("Basic account")

class SavingsAccount(Account):
    def savings(self):
        print("Savings account interest")

class FixedDepositAccount(SavingsAccount):
    def fd(self):
        print("Fixed deposit benefits")

obj = FixedDepositAccount()
obj.info()
obj.savings()
obj.fd()

# 9. Create a class Device → Computer → Laptop and show functionality extension.
class Device:
    def power_on(self):
        print("Device ON")

class Computer(Device):
    def process(self):
        print("Processing data")

class Laptop(Computer):
    def portable(self):
        print("Laptop is portable")

l = Laptop()
l.power_on()
l.process()
l.portable()

# 10. Write a program where each class in multilevel inheritance modifies a variable and shows
class A:
    def __init__(self):
        self.value = 10

class B(A):
    def __init__(self):
        super().__init__()
        self.value += 5

class C(B):
    def __init__(self):
        super().__init__()
        self.value *= 2

obj = C()
print("Final value =", obj.value)