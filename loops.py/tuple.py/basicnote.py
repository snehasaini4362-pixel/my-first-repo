# convert a tuple into list
t=(1,3,4)
print(type(t))
li=list(t)
li.append(7)
print(t)
print(tuple(li))

t=(1,2,3,4,5,6,7,8,9,10,11,12,13)
even=()
odd=()
for i in t:
    if i%2==0:
        even=even+(i,)
    else:
        odd=odd+(i,)   
print(even)
print(odd)     

t=(1,2,3,4,5,6,7,8,9,10,11,12,13)
max=t[0]
for i in t:
    if max<i:
        max=i
print(max)     

t=(1,2,3,4,5,6,7,8,9,10,11,12,13)
largest=even[0]
even=()
for i in t:
    if i %2==0:
        even=even+(i,)
for i in even:
    if i>largest:
        largest=i
print(even)
print(largest)    

t=(1,2,3,4,5,6,7,8,9,10,11,12,13)
smallest=odd[0]
odd=()
for i in t:
    if i % 2!=0:
        odd=odd+(i,)
for i in odd:
    if i<smallest: 
        i=smallest
print(odd)
print(smallest)               







