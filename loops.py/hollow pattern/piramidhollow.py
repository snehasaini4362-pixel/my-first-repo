n=5
for i in range(1,n+1):
    print(" "*(2*(n-i)),end=" ")
    for j in range(1,2*i):
        if j==1  or i==n or j==2*i-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()            
