
# 1.
# s= "hello world"
# print(s[0:5])



# 2.
# s= input("enter a string:")
# print(s[1:-1])


# 3.
# s="pythonprogramming"
# python=s[0:6]
# programming=s[6:17]
# print(python)
# print(programming)

# 4.
# s="apple"
# print(s[::-1])



5
# print even index(2,4,6,8,10)
# s=input("enter a string")
# print(s[0:10])
6
#print odd index(1,3,5,7,9) 
# s=input("enter a string:")
# print(s[0:10])
7
# s="learningpython"
# python=(s[-6:])
# print(python)




# 8
# s= "datascience"
# science=(s[4:])
# print(science)

# 9
# s=input("enter a string:")
# n=int(input("enter a n:"))
# print(s[:n])

# 10
# s="slicingExamples"
# print(s[0:15:2])

# 11
# s=input("enter a string")
# print(s[3:-3])

# 12
# s="abcdefghijklmnop"
# print(s[6:11])




# 13
# s=input("enter a string:")
# last_four=s[-4:]
# print("last 4 characters:",last_four)

# 14
# s="OpenAIChatGPT"
# print(s[0:7])

# print(s[4:10])

# print(s[::-1])

# 15
# s=input("enter a string")
# print(s[2:-2])

# 16
# s="ABCDEFG"
# print(s[0:7:2])

# 17
# s="HelloPython"
# print(s[3:7])


# first_name=input("enter a first name").title()
# last_name=input("enter a last name").title()
# # full_name=first_name + last_name
# print(first_name,last_name)














# if-else assignment:-
# 1.
# n=int(input("enter a number:"))
# if(n%2==0):
#     print('even')
# else:
#     print('odd')

# 2.
# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# c = float(input("Enter third number: "))

# if a >= b and a >= c:
#     largest = a
# elif b >= a and b >= c:
#     largest = b
# else:
#     largest = c

# print("Largest number is:", largest)
# 3.
# year=int(input("enter the year"))
# if(year%400==0) or (year%4==0 and year%100!=0):
#     print(year,"leap year")
# else:
#     print(year,"not a leap year")

# s="sneha"
# print(s.upper())

# s="sneha"
# print(s.lower())
# s="sneha saini"
# print(s.capitalize())
# s="  sneha "
# print(s.rstrip())

# s="sneha"
# print(s.title())

# s="my name is kanishka"
# print(s.split())

# print(s.join(s))

# password=input("enter your password:")
# if password.isalpha():
#     print("correct")
# else:  
#     print("wrong")  

# password=input("enter your password:")
# if password.isspace():
#     print("correct")
# else:
#     print("wrong")    

# s=input("enter a character ")
# if s.endswith('bye'):
#     print("this is correct")

# age=input("enter your age")
# name=input("enter your name")
# # print(f'hello my name is{name}.i am {age}year old')    
# print('hello my name is { }.i am { } year old: format(name,age)')


# s="hello world"
# print(s[0:5])


# s=input("enter a character")
# if s.startswith('hello'):
#     print('this starts with hello')
 
# s=input("enter a string")
# if s.endswith('.com'):
#     print('this ends with .com')

# s=input("enter a string")
# if s.startswith('py') and s.endswith('on'):
#     print('this starts with "py" and ends with "on"')


# s=input("enter a string:")
# if s.isalpha():
#     print('only alphabets')

# s=input("enter a string:")
# if s.isdigit():
#     print('only digits')


# s=input("enter a string")
# if s.isalnum():
#     print('alpha and numeric')

# s=input("enter a string")
# if s.isspace():
#     print('space')

# name=input("enter your name")
# if name.isalpha():
#     print('valid name')
# else:
#     print('not valid')    

# number_plate=input("enter vehicle number plate")
# if number_plate.isalnum():
#     print('number plate is correct')




# first_name=input("enter first name:")
# last_name=input("enter last name:")
# full_name=first_name+' '+last_name
# print(full_name.title())

# n=input("enter your name")
# print(n*5)


# first_name=input("enter first name:")
# last_name=input("enter last name:")
# full_name=first_name+' '+last_name
# print(full_name.title())

# n=input("enter a string")
# print(n*10)

# character=input("enter a character:")
# for ch in character:
#     print(ch)

# s="naman"
# if s==s[::-1]:
#     print('this is a palindrome')
# else:
#     print('not a palindrome')    

# s="elephant"
# print(s[0:8:2])



# length=8
# idigits
# upper characters
# lower character
# special character

# password=input("enter a password:")

# valid_len=len(password)>=8
# has_digit=False
# has_upper=False
# has_lower=False
# has_special=False

# for c in password:
#     if c.isdigit():
#         has_digit=True
#     elif c.isupper():
#         has_upper=True
#     elif c.islower():
#         has_lower=True
#     elif not c.isalnum(): 
#         has_special=True  
        
# if has_digit and has_upper and has_lower and has_special and valid_len:
#     print("strong password")
# else:
#     print("weak password")         



# sentence=input("enter a sentence:")
# vowel="aeiouAEIOU"
# count=0

# words=sentence.split()
# for c in words:
#     if c[0] in vowel and c[-1] in vowel:
#         count += 1
#         print('count')    



# sentence=input("enter a sentence:")

# words=sentence.split()
# print("palindrome word:")
# for w in words:
#     if w==w[::-1]:
#         print(w)


# s=input("enter a string")
# prime_number='2357'
# count=0
# for c in s:
#     if c in prime_number:
#         count+=1
#         print(count)

# s= input("enter a string")
# count=0
# for c in s:
#     if c.isdigits():
#         count+=1
#         print("sum of digits=",count)

#         rev = ""
# for ch in s:
#     rev = ch + rev

# print("Reversed string =", rev)


# n="naman"
# s=input("enter a string")
# if n==s[::-1]:
#     print('palindrome')
# else:
#     print('not a palimdrome')    



# user=int(input("enter a number"))
# if  user%2==0:
#     print("even")
# else:
#     print("odd")    


# a=int(input("enter a first number"))
# b=int(input("enter a second number"))
# c=int(input("enter a third number"))
# if a>b and a>c:
#     largest= a
# elif b>a and b>c:
#     largest=b
# else:
#      largest=c
# print("largest number is:",largest)


# year=int(input("enter a year"))
# if year%400==0 or year%4==0 and year%100!=0:
#     print("leap year" )
# else:
#     print("not a leap year")     

# n=int(input("enter a percentage:"))
# if n>=90:
#     print('GRADE A')
# elif n>=80:
#     print('GRADE B') 
# elif n>=70:
#     print('GRADE C')
# elif n>=60:
#     print('GRADE D')
# else:
#     print('fail') 
# n=input("enter a string:")
# vowels="aeiouAEIOU"
# if n in vowels:
#     print("vowel")
# else:
#     print("consonent")     

# a=float(input("enter a number:"))
# b=float(input("enter a number:"))
# op=input("enter a op(+-*/):")

# if op=="+":
#     print("result=",a+b)
# elif op=="-":
#     print("result=",a-b)
# elif op=="*":
#     print("result=",a*b)
# elif op=="/":
#     print("result=",a/b)
# else:
#     print("division by zero is not allowed")                

# n=int(input("enter a number"))
# if n>0:
#     print("positive")
# elif n<0:
#     print("negetive")
# else:
#     print("zero")

# username=input("enter a password")
# password=input("enter a password")

# if username=="admin" and password=="1234":
#     print('login succesfull')
# else:
#     print("not a valid password")

# a=int(input("enter a first side"))
# b=int(int("enter a second side"))
# c=int(int("enter a third side"))

# if (a+b>c and b+c>a and a+c>a):
#     print("triagle")
# else:
#     print("not a valid triagle")        
        
# price=float(input("enter a price of the  product:"))
# if price>1000:
#     discount=price*0.10
# elif price>=500 and price<=1000:
#     discount=price*0.05  
# else:
#     discount=0
# final_price=price-discount
# print("final price after discount",final_price)  

# month=input("enter a month:")
# year=int(input("enter a year:"))

# if month=="january" or  month=="march" or month=="may" or month=="july"or month=="august" or month=="october" or month=="december":
#     print("31 days")
# elif month=="april" or month=="june" or month=="september" or month=="november":
#     print("30 days")
# elif month=="february":
#     if(year%400==0 ) or (year%4==0 and year%100!=0):
#         print("29 days")
#     else:
#         ("28 days")
# else:
#     print("invalid year")            

# age=int(input("enter a age:"))
# if age>=0 and age<=1:
#     print("infant")
# elif age>=2 and age<=4:
#     print("toddler")
# elif age>=5 and age<=12:
#     print("child")
# elif age>=13 and age<=19:
#     print("teenager")
# elif age>=20 and age<=59:
#     print("adult")
# elif age>=60:
#     print("senior")
# else:
#     print("invalid age")                      

# n=int(input("enter week(1-7)"))
# if n==1:
#     print("monday")
# elif n==2:
#     print("tuesday")
# elif n==3:
#     print("wednesday")
# elif n==4:
#     print("thursday")
# elif n==5:
#     print("friday")  
# elif n==6:
#     print("saturday") 
# elif n==7:
#     print("sunday")
# else:
#     print("invalid")             

