# qq.1 how many 1 in given list for using loop?
# li=[1,1,1,2,3,4,4,1,1]
# count=0
# for i in li:
#     if i == 1:
#         count+=1
# print(count)        

# qq.2
# rev. a list using a loop 
# li=[1,2,3,4,5]
# rev=[]
# for i in range(len(li)-1,-1,-1):
#     rev.append(li[i])
# print(rev)    

# second method to rev. a list using dsa 
# li=[1,2,3,4,5]
# left=0
# right=len(li)-1
# while left <right:
#     li[left],li[right]=li[right],li[left]
#     left+=1
#     right-=1
# print(li)    

# qq.3
# product itself
li=[1,2,3,4]
prod=1
for i in li:
    prod*=i
new_list=[]
for j in range(len(li)):
    self_prod=prod//li[j]
    new_list.append(self_prod)
print(new_list) 

# qq.4 remove duplicate values in list
li=[1,2,1,2,3,4]
common=[]
for i in li:
    if i not in common:
        common.append(i)
print(common)        

# qq.5 max and min 
li=[1,2,3,4,5]
max=li[0]
min=li[0]
for i in range(len(li)):
    if li[i]>max:
        max=li[i]
    elif li[i]<min:
        min=li[i]
print(max)
print(min)

# qq.6 print the index of the target sum=7
li=[1,2,3,4,5]
target=7
for i in range(len(li)):
    for j in range(i+1,len(li)):
        if li[i]+li[j]==target:
            print(i,j)

# qq.7 product of all positive no.
li=[1,-2,3,-4,5]
product=1
for i in li:
    if i > 0:
        product=product*i
print(product)         

# qq.8 2d list  question
li=[[1,2,3],[4,5,6]]
for i in li:
    for j in i:
        print(j,end='')
        

