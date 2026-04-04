# 1. Create a base class Animal with a method sound(). Then create three child classes Dog, Cat, and
# Cow that override the sound() method to print their respective sounds. Write a main program where you
# create objects of each class and call the sound() method using a parent class reference to demonstrate
# runtime polymorphism.

class Animal:
    def sound(self):
        print("bark")

class Dog(Animal):
    def sound(self):
        print("boo")
    
class Cat(Animal):
    def sound(self):
        print("meeow")
class Cow(Animal):
    def sound(self):
        print("mee")

Animals=[Dog(),Cat(),Cow()]

for i in Animals:
    i.sound()
# a1=Dog()
# a2=Cat()
# a3=Cow()

# a1.sound()
# a2.sound()
# a3.sound()

# 2. Create a base class Vehicle with a method start(). Then create child classes Car, Bike, and Truck
# that override the start() method with their own implementation. Demonstrate how the correct method is
# called at runtime when using a common reference.

class Vehicle:
    def start(self):
        print("vehicle start")

class car(Vehicle):
    def start(self):
        print("car start")
class bike(Vehicle):
    def start(self):
        print("bike start")

class Truck(Vehicle):
    def start(self):
        print("truck start")

gadi=[car(),bike(),Truck()] 
for i in gadi:
    i.start()       

# 3. Create a base class Shape with a method area(). Then create child classes Circle and Rectangle.
# Override the area() method in both classes to calculate their respective areas. Use dynamic method
# dispatch to call the correct area() method.
class Shape:
    def area(self):
        print("area not defined")

class Circle(Shape):
    def area(self):
        print("area of circle=3.14*r*r")
class Rectangle(Shape):
    def area(self):
        print("area=length*breadth")
shapes = [Circle(),Rectangle()] 

for i in shapes:
    i.area()    

# 4. Create a base class Employee with a method salary(). Then create subclasses FullTimeEmployee
# and PartTimeEmployee. Override the salary() method in each subclass to calculate salary differently.
# Demonstrate runtime polymorphism using these classes.       
           
class Employee:
    def salary(self):
        print("Salary not defined")

class FullTimeEmployee(Employee):
    def salary(self):
        salary = 30000  
        print("Full Time Employee Salary =", salary)

class PartTimeEmployee(Employee):
    def salary(self):
        hours = 5
        rate = 200
        salary = hours * rate
        print("Part Time Employee Salary =", salary)

employees = [FullTimeEmployee(), PartTimeEmployee()]

for emp in employees:
    emp.salary()

# 5. Create a base class Bank with a method interest_rate(). Then create subclasses SBI, HDFC, and
# ICICI. Each subclass should override the interest_rate() method with different values. Write a program
# to show polymorphic behavior.    

class Bank:
    def interest_rate(self):
        print("Interest rate not defined")

class SBI(Bank):
    def interest_rate(self):
        print("SBI Interest Rate = 6%")

class HDFC(Bank):
    def interest_rate(self):
        print("HDFC Interest Rate = 7%")

class ICICI(Bank):
    def interest_rate(self):
        print("ICICI Interest Rate = 6.5%")

banks = [SBI(), HDFC(), ICICI()]

for b in banks:
    b.interest_rate()

# 6. Create a base class Payment with a method pay(amount). Then create subclasses
# CreditCardPayment, UPIPayment, and CashPayment that override the pay() method with different
# logic. Show how runtime polymorphism works when calling the method.
class Payment:
    def pay(self, amount):
        print("Payment method not defined")

class CreditCardPayment(Payment):
    def pay(self, amount):
        print("Paid", amount, "using Credit Card")

class UPIPayment(Payment):
    def pay(self, amount):
        print("Paid", amount, "using UPI")

class CashPayment(Payment):
    def pay(self, amount):
        print("Paid", amount, "using Cash")

payments = [CreditCardPayment(), UPIPayment(), CashPayment()]

for p in payments:
    p.pay(1000)

# 6. Create a base class Payment with a method pay(amount). Then create subclasses
# CreditCardPayment, UPIPayment, and CashPayment that override the pay() method with different
# logic. Show how runtime polymorphism works when calling the method.    

class Payment:
    def pay(self):
        print("Payment")

class CreditCard(Payment):
    def pay(self):
        print("Paid by Credit Card")

class UPI(Payment):
    def pay(self):
        print("Paid by UPI")

class Cash(Payment):
    def pay(self):
        print("Paid by Cash")

for p in [CreditCard(), UPI(), Cash()]:
    p.pay()

# 7. Create a base class Notification with a method send(message). Then create subclasses
# EmailNotification, SMSNotification, and PushNotification. Each subclass should override the send()
# method. Demonstrate polymorphism using a loop.
class Notification:
    def send(self):
        print("Sending notification")

class Email(Notification):
    def send(self):
        print("Email sent")

class SMS(Notification):
    def send(self):
        print("SMS sent")

class Push(Notification):
    def send(self):
        print("Push notification sent")

for n in [Email(), SMS(), Push()]:
    n.send()

# 8. Create a base class Media with a method play(). Then create subclasses Audio, Video, and Podcast.
# Override the play() method in each subclass. Show how different play() methods are called
# dynamically.
class Media:
    def play(self):
        print("Playing media")

class Audio(Media):
    def play(self):
        print("Playing audio")

class Video(Media):
    def play(self):
        print("Playing video")

class Podcast(Media):
    def play(self):
        print("Playing podcast")

for m in [Audio(), Video(), Podcast()]:
    m.play()

# 9. Create a base class User with a method access_level(). Then create subclasses Admin, Editor, and
# Viewer. Override the access_level() method to return different permissions. Demonstrate runtime
# polymorphism.
class User:
    def access(self):
        print("Basic access")

class Admin(User):
    def access(self):
        print("Full access")

class Editor(User):
    def access(self):
        print("Edit access")

class Viewer(User):
    def access(self):
        print("View only")

for u in [Admin(), Editor(), Viewer()]:
    u.access()


# 10. Create a base class Appliance with a method turn_on(). Then create subclasses Fan, AC, and
# WashingMachine. Override the turn_on() method with specific behavior. Show polymorphism using a
# collection of objects.
class Appliance:
    def turn_on(self):
        print("Appliance on")

class Fan(Appliance):
    def turn_on(self):
        print("Fan on")

class AC(Appliance):
    def turn_on(self):
        print("AC on")

class WashingMachine(Appliance):
    def turn_on(self):
        print("Washing Machine on")

for a in [Fan(), AC(), WashingMachine()]:
    a.turn_on()


# 11. Create a base class Account with a method withdraw(amount). Then create subclasses
# SavingsAccount and CurrentAccount. Override withdraw() with different rules such as minimum
# balance or overdraft. Demonstrate runtime polymorphism.
class Account:
    def withdraw(self):
        print("Withdraw")

class Savings(Account):
    def withdraw(self):
        print("Min balance required")

class Current(Account):
    def withdraw(self):
        print("Overdraft allowed")

for a in [Savings(), Current()]:
    a.withdraw()

# 12. Create a base class GameCharacter with a method attack(). Then create subclasses Warrior,
# Mage, and Archer. Override attack() with different behaviors. Show dynamic method selection at
# runtime.
class GameCharacter:
    def attack(self):
        print("Attack")

class Warrior(GameCharacter):
    def attack(self):
        print("Sword attack")

class Mage(GameCharacter):
    def attack(self):
        print("Magic attack")

class Archer(GameCharacter):
    def attack(self):
        print("Arrow attack")

for g in [Warrior(), Mage(), Archer()]:
    g.attack()

# 13. Create a base class FileHandler with a method open(). Then create subclasses TextFile, ImageFile,
# and PDFFile. Override open() to simulate opening different file types. Demonstrate runtime
# polymorphism.
class FileHandler:
    def open(self):
        print("Opening file")

class TextFile(FileHandler):
    def open(self):
        print("Opening text file")

class ImageFile(FileHandler):
    def open(self):
        print("Opening image file")

class PDFFile(FileHandler):
    def open(self):
        print("Opening PDF file")

for f in [TextFile(), ImageFile(), PDFFile()]:
    f.open()

# 14. Create a base class Transport with a method fare(distance). Then create subclasses Bus, Train,
# and Taxi. Override fare() with different fare calculation logic. Show polymorphism using different
# objects.
class Transport:
    def fare(self):
        print("Fare")

class Bus(Transport):
    def fare(self):
        print("Bus fare")

class Train(Transport):
    def fare(self):
        print("Train fare")

class Taxi(Transport):
    def fare(self):
        print("Taxi fare")

for t in [Bus(), Train(), Taxi()]:
    t.fare()

# 15. Create a base class SmartDevice with a method operate(). Then create subclasses SmartLight,
# SmartTV, and SmartSpeaker. Override operate() to perform device-specific actions. Demonstrate
# runtime polymorphism using a list of objects.
class SmartDevice:
    def operate(self):
        print("Operating device")

class SmartLight(SmartDevice):
    def operate(self):
        print("Light on")

class SmartTV(SmartDevice):
    def operate(self):
        print("TV on")

class SmartSpeaker(SmartDevice):
    def operate(self):
        print("Speaker on")

for d in [SmartLight(), SmartTV(), SmartSpeaker()]:
    d.operate()