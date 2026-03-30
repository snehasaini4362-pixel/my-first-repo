# q.1. Create a class Person with a private variable __name. Create methods to set and get the name.
class person:
    def __init__(self,name):
        self.__name=name
    def dispaly(self):
        print(f'person name :{self.__name}')
    def display_name(self):
        name=self.__name
        print(name) 
    def new_name(self,new):
        self.__name=new
        print("name changed sucessfully")

obj1=person("sneha")
# obj1.dispaly()
obj1.display_name()
obj1.new_name("sanjana")
obj1.display_name()

# q.2Create a class BankAccount with private variable __balance. Add methods deposit(amount),
# withdraw(amount), and get_balance().
class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    def dispaly(self):
        print(f'balance:{self.__balance}')

    def deposit(self,amount):
        self.__balance +=amount
        print("amount deposite successfully")

    def withdraw(self,new_amount):
        self.__balance-=new_amount
        print("amount withdraw sucessfully ")  

    def total_amount(self):
        balance=self.__balance
        # print(balance)    
per1=BankAccount(500)
per1.dispaly()
per1.deposit(1000)
per1.dispaly()
per1.withdraw(200)
per1.dispaly()
per1.total_amount()
print(per1._BankAccount__balance)

# q.3Create a class Student with private variable __marks. Add methods to assign and display marks
# only if marks are greater than 0.
class student:
    def __init__(self):
        self.__marks=0
    def set_marks(self,marks):
        if marks>=0:
            self.__marks=marks
        else:
            print("marks should be greter than 0")
    def get_marks(self):
        return self.__marks

s=student()
s.set_marks(50)
print(s.get_marks())
s.set_marks(-10)

# q.4Create a class Employee with private variable __salary. Add methods to set salary, increase
# salary by percentage, and get salary.
class employee:
    def __init__(self):
        self.__salary=0
    def set_salary(self,salary):
        self.__salary=salary
    def add_percent(self,percentage):
        self.__salary+=self.__salary*percentage/100

    def get_salary(self):
        return self.__salary

e=employee()
e.set_salary(10000)
e.add_percent(10)

print(e.get_salary())

# q.5 Create a class Temperature with private variable __celsius. Add methods to set temperature and
# convert it to Fahrenheit.
class  Temperature:
    def __init__(self):
        self.__celsius=0

    def set_celsius(self,c):
        self.__celsius=c

    def to_fahrenheit(self):
        return(self.__celsius*9/5)+32

t=Temperature()
t.set_celsius(25)
print(t.to_fahrenheit())

# q.6 Create a class Mobile with private variable __price. Add methods to 
# set price (not negative) and get price.
class Mobile:
    def __init__(self):
        self.__price=0

    def set_price(self,p):
        if p>=0:
            self.__price=p
        else:
            print("price cannot ba negetive")

    def get_price(self):
        return self.__price

m=Mobile()
m.set_price(15000)
print(m.get_price())

m.set_price(-500)

# q.7 Create a class Car with private variable __speed. Add methods set_speed(speed <= 200) and
# get_speed().
class car:
    def __init__(self):
        self.__speed=0
    
    def set_speed(self ,s):
        if s<=200:
            self.__speed=s
        else:
            print("speed limit is 200")

    def get_speed(self):
        return  self.__speed

obj1=car()
obj1.set_speed(150)
print(obj1.get_speed())

obj1.set_speed(250)

# q.8Create a class LoginSystem with private variable __password. Add methods to set and validate
# password.
class LoginSystem:
    def __init__(self):
        self.__password=""

    def set_password(self,p):
        self.__password=p
    def validate_password(self,p):
        if p == self.__password:
            print("login sucessfull")
        else:
            print("wrong password")        
obj1=LoginSystem()   
obj1.set_password("snu123")
obj1.validate_password("snu123")
obj1.validate_password("343yhg")  

# q9. Create a class Product with private variable __quantity. Add methods to add stock, reduce stock
# (not below 0), and check quantity.
class product:
    def __init__(self):
        self.__quantity=0

    def add_stock(self,a):
        self.__quantity+=a

    def reduce_stock(self,r):
        if  self.__quantity-r >=0:
            self.__quantity-=r
        else:
            print("not enough stock")    
    def get_quantity(self):
        return self.__quantity  

p=product()
p.add_stock(50)
p.reduce_stock(20)
print(p.get_quantity())

p.reduce_stock(40)

# q.10Create a class VotingSystem with private variable __age. Add methods to set age and check if
# user can vote (>=18).
class VotingSystem:
    def __init__(self):
        self.__age=0
    
    def set_age(self,a):
        self.__age=a

    def can_vote(self):
        if self.__age>=18:
            print("you can vote ")
        else:
            print("you cannot vote")  

v=VotingSystem()
v.set_age(20)
v.can_vote()

v.set_age(15)
v.can_vote()





