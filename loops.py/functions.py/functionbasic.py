def is_even(n):
    if n%2==0:
        return True
    return False
if is_even(2):
    print("even no.")
else:
    print("odd no.")  

# prime or not
def is_prime(n):
    fact=0
    for i in range(1,n+1):
        if n%i==0:
            fact+=1
    if fact==2:
        return True
    else:
        return False            
if is_prime(14):
    print("prime no.")
else:
    print("not prime")    

# print prime no 2 to 100
def is_prime(n):
    fact=0
    for i in range(1,n+1):
        if n%i==0:
            fact+=1
    if fact==2:
        return True
    return False
for i in range(2,101):
    if is_prime(i):
        print(i)   

# qq. palindrome or not          

def is_palindrome(n):
    temp=n
    rev=0
    while(n!=0):
        digit=n%10
        rev=rev*10+digit
        n=n//10
    if temp==rev:
        return True
    else:
        return False
if is_palindrome(121):
    print("palindrome")
else:
    print("not palindrome")


#   qq. print palindrome      
  def is_palindrome(n):
    for i in range(1,n+1):
        temp=i
        rev=0
        while(temp!=0):
            digit=temp%10
            rev=rev*10+digit
            temp=temp//10
        if i==rev:
            print(i)
is_palindrome(100)       
      
   
                                                