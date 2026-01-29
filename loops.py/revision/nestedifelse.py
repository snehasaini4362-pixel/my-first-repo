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