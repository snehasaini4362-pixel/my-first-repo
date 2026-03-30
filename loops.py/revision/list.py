# qq.1 find the largest number in list
li=[1,2,3,4]
max=li[0]
for i in range(len(li)):
    if li[i]>max:
        max=li[i]
print(max)   

# qq.2 seprate out even and odd element in list
li=[1,2,3,4,5,6,7]
even=[]
odd=[]
for i in li:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)

# qq.3product of all the element in list
li=[1,2,3,4]
prod=1
for i in li:
    prod*=i
print(prod)    

# qq.4count how many occurances 
li=[1,2,3,4,1,1,1]
count=0
for i in li:
    if i==1:
        count+=1
print(count)        

# qq.5 reverse a list  
li=[1,2,3,4,5,6]
# rev=[]
# for i in range(len(li)-1,-1,-1):
#     rev.append(li[i])
# print(rev)
left=0
right=len(li)-1
while(left<right):
    li[left],li[right]=li[right],li[left]
    left+=1
    right-=1
print(li)    

# qq.6product of all odd elements in list 
li=[1,2,3,4,5,6,7]
prod=1
for i in li:
    if i %2!=0:
        prod*=i
print(prod)        
    
# qq.7 selfprod
li=[1,2,3,4]
prod=1
for i in li:
    prod*=i
print(prod) 
new_list=[]
for j in range(len(li)):
    self_prod=prod//li[j]
    new_list.append(self_prod)
print(new_list)    

# qq.8 how many even no. in list
li=[1,2,3,4,5,6]
even=[]
for i in li:
    if i % 2==0:
        even.append(i)
print(even)        

# qq.9 count how many even numberes in list
li=[1,2,3,4,5,6]
count=0
for i in li:
    if i % 2==0:
        count+=1
print(count)        
        

# qq.10 common elements in list
li1=[1,2,3,4,5]
li2=[3,4,5,6,7]
common=[]
for i in li1:
    if i in li2:
        common.append(i)
print(common)        

# qq.11find unique elements
li1=[1,1,1,2,3,2,3,4,5]
unique=[]
for i in li1:
    if i not in unique:
        unique.append(i)
print(unique)        

# qq.12 find min and max in list
li=[1,2,3,4,5]
min=li[0]
max=li[0]
for i in range(len(li)):
    if min>li[i]:
        min=li[i]
    elif max<li[i]:
        max=li[i]
print(min)
print(max)

# qq.13 find second largest no, in list
li=[1,2,3,4,5]
first=li[0]
second=li[0]
for i in range(len(li)):
    if first < li[i]:
        second = first
        first=li[i]
    elif second>li[i]:
        second=li[i]
print(second)        

# qq.14 reverse the whole sentence
word='this is a sentence'.split() 
new=[]
for i in word:
    new.append(i[::-1])
print(" ".join(new))    

# qq.15 find the frequency of each elements in list
li=[1,1,1,2,2,2,3,4,5]
count=[]
for i in li:
    if i not in count:
        count.append(i)
for i in count:        
    print(i,":",li.count(i))        

# qq.16 rotate the list
li=[10,20,30,40,50]
k=4
left=0
right=len(li)-1
while (left < right ):
    li[left],li[right]=li[right],li[left]
    left+=1
    right-=1
print(li)    

left=0
right=k-1
while left < right:
    li[left],li[right]=li[right],li[left]
    left+=1
    right-=1
print(li)  

left=k
right=len(li)-1
while left < right:
    li[left],li[right]=li[right],li[left]
    left+=1
    right-=1
print(li)    

# qq.17 find  index occurences
li=[5,2,7,2,9,2]
target=2
new_list=[]
for i in range(len(li)):
    if li[i]==target:
        new_list.append(i)
print(new_list)    

# qq.18 find positive no in list
li=[3,-1,5,-7,8,-2]
negetive=[]
for i in li:
    if i>0:
        negetive.append(i)
print(negetive)        
        
# qq.19 check a list is a palindrome 
li=[1,2,3,2,1]
if li==li[::-1]:
    print("palindrome")
else:
    print("not palindrome")

# qq.20 common elemnets in two list 
list1 = [1, 2, 3]
list2 = [3, 4, 5]
sum=(list1+list2)
print(sum)
new_list=[]
for i in sum:
    if i not in new_list:
        new_list.append(i)
print(new_list) 

# qq.21sum of the target
nums = [2, 4, 3, 5, 7]
target = 7

for i in range(len(nums)) :
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            print((nums[i],nums[j]))
            
# qq.22 find missing number in list
nums = [1, 2, 4, 5, 6]
for i in range(1,7):
    if i not in nums:
        print(i)
# qq.23 do not print duplicate value

nums = [1, 2, 2, 3, 4, 4, 5]
s=[]
for i in nums:
    if nums.count(i)==1:
        s.append(i)
print(s)      

# qq.24 product of postive numbers in list
li = [1, -2, 3, -4, 5]
prod=1
for i in range(len(li)):
    if li[i]>0:
        prod*=li[i]
print(prod)        
        

