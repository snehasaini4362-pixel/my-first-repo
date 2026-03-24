# def example ():
# try:
#     # risky code
# except exception as e:
#     print("error:",e)
# else:
#     print("success")
#         #jab error nhi aaye 
# finally:
#     print("done")
#     # "always run"          

# qq.1
def division(a,b):
    try:
        result=(a/b)
        return result
        
    except exception  as e  :
        print("something  has occured in program",e)
    else:
        print("if no errors occurs")
    finally:
        print("execution completed")  

print(division(10,2))    

# qq.2
def convert_int(a):
    try:
        num=int(a)
        
    except exception  as e  :
        print("something  has occured in program",e)
    else:
        print("the converted value",num)
    finally:
        print("Conversion attempt finished.")  

convert_int("10")

# qq.3
def square_of_num(a):
    try:
        num=float(a)
        
    except exception  as e  :
        print("something  has occured in program",e)
    else:
        return num*num
    finally:
        print("to display process done ")  

print(square_of_num(4))    

# qq.4
def floor(a,b):
    try:
        result=(a//b)
        
    except exception  as e  :
        print("something  has occured in program",e)
    else:
        print("quotient",result)
    finally:
        print("functuon executed ")  

print(floor(10,3))    

# qq.5
def reciprocal(a):
    try:
        num=float(a)
        result=(1/num)
        
    except exception  as e  :
        print("something  has occured in program",e)
    else:
       print(" the reciprocal")
    finally:
        print("end of opertion")  

reciprocal(2)  

# qq.6
def multiple(a,b):
    try:
        x=int(a)
        y=int(b)
        
        
    except exception  as e  :
        print("something  has occured in program",e)
    else:
       print(" product",x*y)
    finally:
        print("multiplication tried")  

print(multiple("2","4"))  

# qq.7
def percentage(marks,total):
    try:
        result=(marks/total)*100
        
    except exception  as e  :
        print("something  has occured in program",e)
    else:
        print("percentage:",result)
    finally:
        print("calcution finished ")  

percentage(80,100)    

# qq.8
def half_value(x):
    try:
        num=float(x)
        result=num/2
    except exception  as e  :
        print("something  has occured in program",e)
    else:
        print("output:",result)
    finally:
        print("completion meassage ")  

half_value("10")

# qq.9
def modulus(a,b):
    try:
        result=(a%b)
        
    except exception  as e  :
        print("something  has occured in program",e)
    else:
        print("remainder:",result)
    finally:
        print("modules attempt done ")  

modulus(10,3)

# qq.10
def power(a,b):
    try:
        result=a**b
        
    except exception  as e  :
        print("something  has occured in program",e)
    else:
        print("power:",result)
    finally:
        print(" power functuon executed ")  

power(2,3)    

# qq.11
def absolute(a):
    try:
        num=float(a)
        result=abs(num)
        
    except exception  as e  :
        print("something  has occured in program",e)
    else:
        print("absolute value:",result)
    finally:
        print(" absolute check completed ")  

absolute(-5)    

# qq.12
def power(a,b,c):
    try:
        result=a/b/c
        
    except exception  as e  :
        print("something  has occured in program",e)
    else:
        print("final result:",result)
    finally:
        print(" division process ended ")  

power(20,2,2)    

# qq.13 double value
def double(a):
    try:
        num=int(a)
        result=num*2
        
    except exception  as e  :
        print("something  has occured in program",e)
    else:
        print("double:",result)
    finally:
        print(" done ")  

double("6")    

# qq.14 substraction
def substraction(a,b):
    try:
        a=int(a)
        b=int(b)
        result=a-b
        
    except exception  as e  :
        print("something  has occured in program",e)
    else:
        print("difference:",result)
    finally:
        print(" substraction attempt finised ")  

substraction("10","4")    

# qq.15 average
def average(a,b):
    try:
        result=(a+b)/2
        
    except exception  as e  :
        print("something  has occured in program",e)
    else:
        print("average:",result)
    finally:
        print(" average calculation done ")  

average(10,20)    

# qq.16 simple interset
def simple_interest(p,r,t):
    try:
        result=(p*r*t)/100
        
    except exception  as e  :
        print("something  has occured in program",e)
    else:
        print("interest:",result)
    finally:
        print("interest calculation done")  

simple_interest(1000,5,2)    

# qq.17self division
def self_division(a):
    try:
        result=a/a
        
    except exception  as e  :
        print("something  has occured in program",e)
    else:
        print("result:",result)
    finally:
        print(" self division completed ")  

self_division(5)    

# qq.18remainder after integer conversion
def remainder(a,b):
    try:
        x=int(a)
        y=int(b)
        result=x%y
        
    except exception  as e  :
        print("something  has occured in program",e)
    else:
        print("remainder:",result)
    finally:
        print(" remainder opertion finished ")  

remainder("9","2")    

# qq.19  multiplication of three number
def multiply_three(a,b,c):
    try:
        result=a*b*c
        
    except exception  as e  :
        print("something  has occured in program",e)
    else:
        print("product:",result)
    finally:
        print(" multiplication process completed ")  

multiply_three(2,3,4)    












  






