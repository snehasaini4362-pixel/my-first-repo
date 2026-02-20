# qq.1
li=[[1,2,3],[4,5,6],[7,8,9]]
for i in li:
    for j in i:
        print(j,end='')

# qq.2
li=[[1,2,3],[4,5,6],[7,8,9]]
sum=0
for i in li:
    for j in i:
        sum+=j
print(sum)

# qq.3
li=[[1,2,3],[4,5,6],[7,8,9]]
max=li[0][0]
for i in li:
    for j in i:
        if j>max:
            max=j
print(max)

# qq.4
li=[[1,2,3],[4,5,6],[7,8,9]]
max=li[0][0]
for i in li:
    for j in i:
        if j>max:
            max=j
print(max)

# qq.5
li=[[1,2,3],[4,5,6],[7,8,9]]
min=li[0][0]
for i in li:
    for j in i:
        if j<min:
            min=j
print(min)

# qq.6
li=[[1,2,3],[4,5,6],[7,8,9]]
count=0
for i in li:
    count+=len(i)
print(count)

# qq.7
li=[[1,2,3],[4,5,6],[7,8,9]]
for i in li:
    print(i)

# qq.8
li=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(li[0])):
    column=[]    
    for j in range(len(li)):
        column.append(li[j][i])
    print(column) 

# qq.9
li=[[1,2,3],[4,5,6],[7,8,9]]
for i in li:
    sum=0
    for j in i:
        sum+=j
    print(sum)    

# qq.10
li=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(li[0])):
    sum=0
    for j in range(len(li)):
        sum+=li[j][i]
    print(sum) 

# qq.11
li=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(li)):
    print(li[i][i])

# qq.12
li=[[1,2,3],[4,5,6],[7,8,9]]
n=len(li)
for i in range(len(li)):
    print(li[i][n-i-1])

# qq.13
li=[[1,2,3],[4,5,6],[7,8,9]]
n=len(li)
sum=0
for i in range(n):
    sum+=li[i][i]
    sum+=li[i][n-i-1]
print(sum)   

# qq.14
li=[[1,2,3],[4,5,6],[7,8,9]]
count=0
for i in li:
    for j in i:
        if j%2==0:
            count+=1
print(count) 

# qq.15
li=[[1,2,3],[4,5,6],[7,8,9]]
count=0
for i in li:
    for j in i:
        if j%2!=0:
            count+=1
print(count)        

# qq.16
li=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(li)):
    for j in range(len(li[i])):
        if li[i][j]<0:
            li[i][j]=0
print(li)     

# qq.17
li=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(li)):
    for j in range(len(li[i])):
        if li[i][j]==5:
            print(i,j)

# qq.18
li=[[1,2,3],[4,5,6],[7,8,9]]
num=5
found=False
for i in li:
    if num in i:
        found=True
        break
print(found)   

# qq.19
li=[[1,2,3],[4,5,6],[7,8,9]]
new_list=[]
for i in li:
    for j in i:
        new_list.append(j)
print(new_list)        







    

       