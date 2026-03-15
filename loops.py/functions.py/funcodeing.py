# q.1 sum of two number
def add(a,b):
    return(a+b)
print(add(20,10))

# q.2 square
def square(n):
    return (n*n)
print(square(4))  

# q.3cube
def cube (n):
    return(n**3)
print(cube(3))   

# q.4 even and odd 
def even_odd(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
print(even_odd(6))    

# q.5 factorial
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
print(factorial(5))   

# q.6 large number
def large_number(a,b):
    if a>b:
        return a
    else:
        return b
print(large_number(10,7))   

# q.7 smallest of three numbers
def smallest(a,b,c):
    return min(a,b,c)
print(smallest(5,2,6))  

# q.8 reverse 
def reverse(n):
    return int(str(n)[::-1])
print(reverse(1234))   

def rev(n):
    rev=0   
    while(n>0):
        digit=n%10
        rev=rev*10+digit
        n=n//10
    return rev    
print(rev(1234))        

# q.9 sum of  digits
def sum_digit(n):
    s=0
    while(n>0):
        digit=n%10
        s+=digit
        n=n//10
    return s
print(sum_digit(123))  

# q.10 palindrome number
def palindrome(n):
    temp=n
    rev=0
    while(n>0):
        digit=n%10
        rev=rev*10+digit
        n=n//10
    if temp==rev:
        return True 
    else:
        return False  
print(palindrome(121))      

# q.11 count digit
def count(n):
    count=0
    while(n>0):
        count+=1
        n=n//10
    return count
print(count(4567))        

# q.12 last digit
def last_digit(n):
    return n%10
print(last_digit(4567))    

# q.13 first digit
def first_digit(n):
    while (n>=10):
        n=n//10
    return n
print(first_digit(4567))        

# q.14
def prime(n):
    for i in range(2,n):
        if i % 2== 0:
            return True
        return False
print(prime(7))  

# q.15 product 
def prod(a,b):
    return a*b
print(prod(4,5))    

# q.16 remainder
def remainder(a,b):
    return a%b
print(remainder(10,3))    

# q.17 sum from 1 to n 
def sum_n(n):
    s=0
    for i in range(1,n+1):
        s+=i
    return s
print(sum_n(5))     

# q.18 multiplication
def multiplication(n):
    result = []
    for i in range(1,11):
        result.append(n*i)
    return result

print(multiplication(5))

# q.19 power
def power(a,b):
    return a**b
print(power(2,3)) 

# q.20
def abs_diff(a,b):
    return abs(a-b)
print(abs_diff(10,4))    
