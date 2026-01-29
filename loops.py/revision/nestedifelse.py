# q.1
n=int(input("enter a number:"))
if n>0:
    print("positive")
    if n%2==0:
        print("even")
    else:
        print("odd")
    
elif n<0:
    print("negetive")
else:
    print("zero")                

# qq.2
# n=int(input("enter number:"))
# if n<10 and n>50:
#     print("outside range")
# else:
#     print("inside range")

# qq.3
# age=int(input("enter age:"))
# if age>=18:
#     if age < 60:
#         print("eligible to vote and not senior citizen")
#     else:
#         print("senior citizen")
# else:
#     print("not eligible to vote")

# qq.4
# year=int(input("enter year:"))
# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print("leap year")
#         else:
#             print("not leap year" )
#     else:
#         print("leap year")
# else:
#     print(" not leap year")
    
# qq.5
# ch=input("enter a character:")
# if ch.isalpha():
#     if ch in 'aeiou':
#         print("alphabet and vowel")
#     else:
#         print("alphabet but not vowel")
# else:
#     print("not an alphabet")

# qq.6
# n=int(input("enter a number:"))
# if(n%4==0 and n%6!=0 ) or (n%6==0 and n%4!=0):
#     print("valid no.")
# else:
#     print("invalid no.")

# qq.7
# a=int(input("enter a number1:"))
# b=int(input("enter a number2:"))
# c=int(input("enter a number3:"))
# if a >=40:
#     if b>=40:
#         if c>=40:
#             print("passed in all")
#         else:
#             print("failed")
#     else:
#         print("failed")
# else:
#     print("failed")

# qq.8
# n=int(input("enter a number:"))
# if n>=100 and n<=999:
#     if n % 2 == 0:
#         print("valid no.")
#     else:
#         print("not even")
# else:
#     print("out of range")

# qq.9
# n=input("enter a char:")
# if n.isalpha():
#     print("alphabet")
# else:
#     print("not a alpha")

# qq.10
temp=int(input("enter a temp:"))
if temp >=20 and temp<=30:
    print("comfortable temp")
else:
    print("not confortable")
    
# qq.11
n=int(input("enter a number:"))
if n % 2 == 0:
    print("divisible by 2 ")
if n % 3 == 0 :
    print("divisible by 3")
if n % 5 == 0:
    print("divisible by 5")
    
# qq.12
age=int(input("enter a number:"))
income=int(input("enter a number:"))
if age >= 21:
    if income >=20000:
        print("eligible for loan")
    else:
        print ("income too low")
else:
    print("age not eligible")
    
# qq.13
n=input("enter a number:")
if n !="":
    if len(n)>8:
        print("valid string")
    else:
        print("length too short")
else:
    print("empty string")

    
    
