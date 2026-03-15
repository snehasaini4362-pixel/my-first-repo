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