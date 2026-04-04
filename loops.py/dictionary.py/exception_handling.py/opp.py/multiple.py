# MULTIPLE INHERITANCE QUESTIONS

# 1. Create two classes Father and Mother with methods skills_father() and skills_mother(). Create a
# child class Child that inherits from both and prints both skills.

class father:
    def skills_father(self):
        print("father skills: driving")
class mother:
    def skills_mother(self):
        print("mother skills: painting")        

class child(father,mother):
    def skills_child(self):
        print("child inherit both parents")

c=child()
c.skills_father()
c.skills_mother()

# 2. Write a program where class Teacher has a method teach() and class Researcher has a method
# research(). Create a class Professor that inherits from both and uses both methods.

class Teacher:
    def teach(self):
        print("teacher teach you")

class Researcher:
    def research(self):
        print("reserchers reserch completed")

class Professor(Teacher,Researcher):
    def display(self):
        print("professer does both teaching and research ")

c=Professor()
c.teach()
c.research()
c.display()    

3. Create two classes Engine and ElectricSystem with respective methods. Create a class
HybridCar that inherits from both and demonstrates both functionalities.

class Engine:
    def engine_type(self):
        print("Petrol Engine")

class ElectricSystem:
    def battery(self):
        print("Electric Battery")

class HybridCar(Engine, ElectricSystem):
    pass

h = HybridCar()
h.engine_type()
h.battery()



# 4. Implement two classes Writer and Speaker with methods write() and speak(). Create a class
# Author that inherits from both and calls both methods.
class Writer:
    def write(self):
        print("Writing books")

class Speaker:
    def speak(self):
        print("Giving speeches")

class Author(Writer, Speaker):
    pass

a = Author()
a.write()
a.speak()


# 5. Create two parent classes Calculator1 (addition) and Calculator2 (multiplication). Create a child
# class that uses both operations.
class Calculator1:
    def add(self, a, b):
        print("Addition =", a + b)

class Calculator2:
    def multiply(self, a, b):
        print("Multiplication =", a * b)

class Calculator(Calculator1, Calculator2):
    pass

c = Calculator()
c.add(2, 3)
c.multiply(2, 3)


# 6. Demonstrate method overriding in multiple inheritance where both parent classes have a method
# with the same name.
class A:
    def show(self):
        print("Class A")

class B:
    def show(self):
        print("Class B")

class C(A, B):
    pass

obj = C()
obj.show() 


# 7. Create a class A and B with constructors. Create class C inheriting from both and show how
# constructors are called.
class A:
    def __init__(self):
        print("Constructor A")

class B:
    def __init__(self):
        print("Constructor B")

class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print("Constructor C")

obj = C()



# 8. Write a program to demonstrate the Method Resolution Order (MRO) in multiple inheritance.
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.mro())



# 9. Create two classes Person and Employee with attributes. Inherit both into Manager and display
# combined details.
class Person:
    def __init__(self, name):
        self.name = name

class Employee:
    def __init__(self, salary):
        self.salary = salary

class Manager(Person, Employee):
    def __init__(self, name, salary):
        Person.__init__(self, name)
        Employee.__init__(self, salary)

    def show(self):
        print("Name:", self.name)
        print("Salary:", self.salary)

m = Manager("Sneha", 50000)
m.show()


# 10. Implement a class SmartDevice that inherits from both Phone and Camera and performs both
# calling and clicking photos.
class Phone:
    def call(self):
        print("Making a call")

class Camera:
    def click(self):
        print("Taking a photo")

class SmartDevice(Phone, Camera):
    pass

s = SmartDevice()
s.call()
s.click()
