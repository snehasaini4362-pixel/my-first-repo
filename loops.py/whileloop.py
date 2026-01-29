# sum=0
# i=1
# while(sum<55):
#     sum=sum+i
#     print("total is:",i,sum)
#     i=i+1    

# a=0
# i=450
# while(a<5):
#     if i%7==0 and i%9==0:
#         a=a+1
#         print("total is:",i,a)
#     i=i-1

# num=7
# i=2
# temp=100
# while(i<num):
#     if (num%i==0):
#         temp=101
#         break
#     i=i+1
# print("condition",temp)    

# question 1:
# n = 10+1
# i = 1
# while(i<n):
#     print(i)
#     i=i+1    

# question 2.
# n = 10
# i = n
# while(i>=1):
#     print(i)
#     i = i - 1

# question 3.
# i = 65
# while(i<=90):
#     print(chr(i),end='')
#     i=i+1

# question 4.
# i = 1
# while(i<=100):
#     if i%2==0:
#         print(i)
#     i=i+1

# question 5.
# n=10
# sum = 0
# i = 1
# while(i <= n):
#     if i%2!=0:
#         sum=sum+i
#     i=i+1 
    
# print("sum of odd number is:",i,sum)
   
# question 6.
# n = 10
# count=0
# while(n!=0):
#     count+=1
#     n//=10

# print(count)

# question 7.

# n=4321
# sum=0
# while (n!=0):
#     digit=n%10
#     sum=sum+digit
#     n=n//10

# print(sum)    

# question 8.

# n=10
# last_digit=n%10

# while(n>=10):
#     n=n//10

# first_digit=n
# print(first_digit)
# print(last_digit)    

n=1234

first= int(n[0])
last =int(n[-1])

sum = first +  last

print(sum)
