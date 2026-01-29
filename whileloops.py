# password='abc'
# while True:
#     user_password=input("enter your password:")
#     if user_password==password:
#         print('login sucessful')
#         break
#     else:
#             print('please enter the valid password')

# question.1
# n=10
# i=1
# while(i<n):
#     print(i)
#     i=i+1

# question.2
# n=10
# while(n>=1):
#     print(n)
#     n=n+1

# question.3
# i=65
# while(i<=90):
#     print(chr(i),end='')
#     i=i+1

# question.4
# n=int(input("enter a number:"))
# i=1
# while(i<=100):
#     if i%2==0:
#         print(i)
#     i=i+1

# question.5
n=int(input("enter a number:"))
sum=0
i=1
while(i<=n):
    if(i%2!=0):
        print(i)
        sum=sum+1
    i=i+1    
print(sum)
        
# question.6
n=123
count=0
while(n!=0):
    count=count+1
    n//=10
print(count)  

# question.7
n=123
sum=0
while(n!=0):
    digit=n%10
    sum=sum+digit
    n=n//10
print(sum)   
# question.8
n=int(input("enter a number:"))
last_digits=n%10
while(n>=10):
    n=n//10
first_digits=n
print("first_digits:",first_digits)
print("last_digits:",last_digits)
# question.9
n=input("enter a number:")
first=int(n[0])
last=int(n[-1])
sum=first+last
print(sum)

# question.10
n=int(input("enter a number:"))
rev=0
while(n!=0):
    digit=n%10
    rev=rev*10+digit
    n=n//10
print(rev)

# question.11
n=int(input("enter a number:"))
p=int(input("enter a number:"))
power=1
i=1
while(i<=p):
    power=power*n
    i=i+1
print(power)

# question.12
n=int(input("enter a number:"))
i=1
while(i<=n):
    if n%i==0:
        print(i)
    i=i+1

# question.13
n=int(input("enter a number:"))
fact=1
i=1
while(i<=n):
    fact=fact*i
    i=i+1
print("factorial",fact)   

# question.14
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
i = 1
while True:
    if (a * i) % b == 0:
        print("LCM =", a * i)
        break
    i = i + 1

# question.15
n=int(input("enter a number:"))
i=2
while(i<n):
    if n%i==0:
        print("not prime")
        break
    i=i+1
else:
    print("prime")
# question.16
n = int(input("Enter a number: "))
num = 2
count = 0
i = 1
while i <= num:
    if num % i == 0:
        count += 1
    i += 1
if count == 2:
    print(num)
num += 1

# question.17
n=int(input("enter a number:"))
i=2
while(i<=n):
    if n%i==0:
        print(i)
        n=n//i 
    else:
        i=i+1
# question.18
n=371
temp=n
total=0
while(n!=0):
    digit=n%10
    total+=digit**3
    n=n//10
print("temp",temp,total) 
if temp==total:
    print("armstrong no.")
else:
    print("not a armstrong no.")
            
# question.19
n = int(input("Enter a number: "))
sum = 0
temp = n
while temp > 0:
    digit = temp % 10

    fact = 1
    i = 1
    while i <= digit:
        fact = fact * i
        i = i + 1

    sum = sum + fact
    temp = temp // 10

if sum == n:
    print("Strong number")
else:
    print("Not a Strong number")

# question.20
 n = int(input("Enter a number: "))
sum = 0
i = 1

while i < n:
    if n % i == 0:
        sum = sum + i
    i = i + 1

if sum == n:
    print("Perfect number")
else:
    print("Not a perfect number")


# question.21
n = int(input("Enter number of terms: "))

a = 0
b = 1
i = 1

while i <= n:
    print(a)
    c = a + b
    a = b
    b = c
    i = i + 1


# question.22
n = 6
sum = 0
i = 1

while i < n:
    if n % i == 0:
        sum = sum + i
    i = i + 1

if sum == n:
    print("Perfect number")
else:
    print("Not a perfect number")

# 0 print nhi hona chaiye

n = 102
new=0
place=1
while n > 0:
    digit = n % 10
    if digit == 0:
        n = n // 10
        continue
    new=new+digit*place
    place=place*10
    n=n//10
print(new)
    

   
        
        
