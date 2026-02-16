n=5
for i in range(0,n):
    print(" "*(2*(n-i)),end=" ")
    for j in range(1,2*i):
        if j==1 or j==2*i-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()            
for i in range(n,0,-1):
    print(" "*(2*(n-i)),end=" ")
    for j in range(1,2*i):
        if j==1 or j==2*i-1:f
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()                