# q.1 lcm question
# a=24
# b=12
# lcm=0
# if a>b:
#     lcm=a
# else:
#     lcm=b
# for i in range(lcm):
#     if (lcm+i)%a==0 and (lcm+i)%b==0:
#         print(lcm+i)
#         break

# q.2 count 
# n=12345
# count=0
# while(n>0):
#     count+=1
#     n=n//10
# print(count)    

# q.3 sum
n=123
sum=0
while(n>0):
    digit=n%10
    sum+=digit
    n=n//10
print(sum)    

# q.4
# febonacci
a=0
b=1
for i in range(5):
    print(a)
    a,b=b,a+b    

# q.5 reverse
n=123
rev=0
while(n>0):
    digit=n%10
    rev=rev*10+digit
    n=n//10
print(rev)  

# q.6 gcd 
a=9
b=12
while(b>0):
    a,b=b,a%b
print(a) 

# q.7 palindrone
n=121 
orginal_num=n
rev=0
while(n>0):
    digit=n%10
    rev=rev*10+digit
    n=n//10
    print(rev)
if orginal_num==rev:
    print("palindrone")
else:
    print("not palindrome")   

# q.8 prime no.
n=7
fact=0
i=1
while(i<=n):
    if i % n==0:
        fact+=1
    i+=1  
if fact==2:
    print("prime no.")
else:
    print("not prime")     

#  q.9sum of even and odd no.
n=1234
even=0
odd=0
while(n>0):
    digit=n%10
    if digit%2==0:
        even+=digit
    else:
        odd+=digit
        n=n//10
print("even")
print("odd")    

# q.10 armstrong no.
n=153
temp=n
rev=0
while(temp>0):
    digit=temp%10
    rev+=digit**3
    temp=temp//10
print(temp) 
if temp==n:
    print("armstrong")
else:
    print("not armstrong") 

# q.11 perfect no.
n=6
sum=0
i=1
while(i<n):
    if n%i==0:
        sum+=i
    i+=1
if sum==n:
    print("perfect no.")
else:
    print("not perfect no.")   

# q.12 count 1  in list
li=[1,1,1,1,2,3,1,1,5,6]
count=0
for i in li:
    if i ==1:
        count+=1
print(count)     

# q.13.rev list
li=[1,2,3,4,5]
rev=0
for i in range(len(li)-1,-1,-1):
    rev.append(li[i])
print(rev)    

li=[1,2,3,4,5]
left=0
right=len(li)-1
while(left < right):
    li[left],li[right]=li[right],li[left]
    left+=1
    right-=1
print(li)    

# q.14 product except self
li=[1,2,3,4]
prod=1
for i in li:
    prod*=i
new_list=[]
for j in range(len(li)):
    self_prod=prod//li[j]
    new_list.append(self_prod)
print(new_list)        

# q.15 repeat value
l1=[1,2,3,4,5]
l2=[3,4,5,6,7]
common=[]
for i in li:
    if l1 in l2:
        common.append(i)
print(common)        

# q.16 min and max
li=[1,2,3,4,5]
max=0
min=0
for i in range(len(li)):
    if li[i]>max:
        li[i]=max
    elif li[i]<min:
        li[i]=min
print(min)
print(max)    

# q.17
li=[2,1,3,4,7,6]
li.sort()
print(li[-1])

li=[2,1,3,4,7,6]
first=0
sencod=0
for i in range(len(li)):
    if li[i]>first:
        first=sencod
        li[i]=first
    elif li[i]<sencod:
        li[i]=sencod
print(second)        






