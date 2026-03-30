# qq.1
class student:
    school_name="GPS"
    def __init__(self, name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f'student name is :{self.name}')
        print(f'student age :{self.age}')    
st1=student("rahul",15)
st2=student("sonam",16)
st3=student("jiya",15)  
st1.display()     
st2.display()
st3.display() 
print(st1.school_name)

# qq.2
class car:
    wheel_set=4
    def __init__(self, brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print(f'brand name is :{self.brand}')
        print(f'price is  :{self.price}')    
cr1=car("ford",5000000)
cr2=car("BMW",6000000) 
cr1.display()     
cr2.display()

# qq.3
class Employee:
    company_name="Amazon"
    def __init__(self,emp_name,salary):
        self.emp_name=emp_name
        self.salary=salary
    def display(self):
        print(f'employee name is :{self.emp_name}')
        print(f'salary :{self.salary}')    
cp1=Employee("rahul",150000)
cp2=Employee("sonam",160000)
cp3=Employee("jiya",150000)  
cp1.display()     
cp2.display()
cp3.display() 

# qq.4
class Mobile:
    category_set="Electronics"
    def __init__(self,Mobile_name,RAM):
        self.Mobile_name=Mobile_name
        self.RAM=RAM
    def display(self):
        print(f'mobile name is :{self.Mobile_name}')
        print(f'RAM :{self.RAM}') 
        print(f'category is :{self.category_set}')   
mob1=Mobile("nokia","2gb ram")
mob2=Mobile("iphone","3gb ram")
mob3=Mobile("vivo","2gb ram")  
mob1.display()     
mob2.display()
mob3.display() 

# qq.5
class book:
    library_name="aaray"
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def display(self):
        print(f'title name is :{self.title}')
        print(f'author:{self.author}') 
        print(f'library_name is :{self.library_name}')   
lb1=book("the guide","R.K Narayan")
lb2=book("harry potter","J.K Rowling") 
lb1.display()     
lb2.display()

# qq.6
class laptop:
    warranty_years=2030
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):    
        print(f'brand name is :{self.brand}')
        print(f'price:{self.price}')
        print(f'warranty year:{self.warranty_years}')
lap1=laptop("lenovo",250000)
lap2=laptop("dell",320000)
lap3=laptop("HP",440000)   
lap1.display()
lap2.display()
lap3.display()    

# qq.7
class person:
    country="India"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f'person name is :{self.name}')
        print(f'age :{self.age}') 
        print(f'country is :{self.country}')   
person1=person("sneha",20)
person2=person("sanjana",21)
person3=person("anjali",22)  
person1.display()     
person2.display()
person3.display() 

# qq.8
class bike:
    wheel_set=2
    def __init__(self,bike_name,mileage):
        self.bike_name=bike_name
        self.mileage=mileage
    def display(self):
        print(f'bike name is :{self.bike_name}')
        print(f'mileage :{self.mileage}') 
        print(f'wheel set is :{self.wheel_set}')   
bike1=bike("splender","65-75 km/l")
bike2=bike("bajaj platina","70-75 km/l")
bike3=bike("honda shine","65 km/l")  
bike1.display()     
bike2.display()
bike3.display() 

# qq.9
class Movie:
    industry_set="bollywood"
    def __init__(self,Movie_name,Rating):
        self.Movie_name=Movie_name
        self.Rating=Rating
    def display(self):
        print(f'movie name is :{self.Movie_name}')
        print(f'rating :{self.Rating}') 
        print(f'industry set  is :{self.industry_set}')   
mov1=Movie("gadar2",8.4/10)
mov2=Movie("3 idiot",5.8/10)
mov3=Movie("dangal",6.9/10)  
mov1.display()     
mov2.display()
mov3.display() 

# qq.10
class Bankaccount:
    bank_name="SBI"
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance
    def display(self):
        print(f'holder name is :{self.account_holder}')
        print(f'balance :{self.balance}') 
        print(f'category is :{self.bank_name}')   
holder1=Bankaccount("sneha",5000)
holder2=Bankaccount("sanjana",4000)
holder3=Bankaccount("riya",6000)  
holder1.display()     
holder2.display()
holder3.display() 





class Bankaccount:
    bank_name="SBI"
    def __init__(self,account_holder,balance,pin):
        self.account_holder=account_holder
        self.__balance=balance
        self._pin=pin
def display(self):
        print(f'holder name is :{self.account_holder}')
        print(f'balance :{self.__balance}') 
        print(f'pin:{self._pin}')
        print(f'category is :{self.bank_name}')
        # getter
def balance_display(self):  
    balance=self.__balance
    print(balance)  
    # setter 
def change_pin(self,newpin):
    self._pin=newpin
    print("pin successfully changed!")            
holder1=Bankaccount("sneha",5000,123)
holder2=Bankaccount("sanjana",4000,234)
holder3=Bankaccount("riya",6000,543)
# dispaly  
holder1.display()     
holder2.display()
holder3.display() 
# check
holder1.balance_display()
# change pin
holder1.change_pin(123456)
holder1.change_pin()
holder2.change_pin(2345)
holder2.change_pin()
holder3.change_pin(5678)
holder3.change_pin()

# qq.2
class employee:
    def __init__(self,name ,designation ,salary, location):
        self.emp_name=name
        self.emp_post=designation
        self.salary=salary
        self.location=location
    def check_salary(self):
        salary=self.__salary
        print(f'the current salary is:{salary}')
    def change_salary(self,new_salary):
        self.__salary=new_salary
        print('new salary updated!')
    emp1=employee('ajay','ml engineer',25,'jaipur')
    emp1.check_salary()
    print(emp1.emp_name)
    print(emp1.emp_post)
    # changed salry
    emp1.change_salary(30)
    # changed salry acess
    emp1.check_salary()            




