# q.1 create a set number 1 to 5 
t={1,2,3,4,5}
print(t)

# q.2 add element to a set
s={1,2,3}
s.add(4)
print(s)

# q.3 remove element
s={1,2,3,4}
s.remove(3)
print(s)

# q.4remove element using discard
s={1,2,3,4}
s.discard(5)
print(s)

# q.5 length of set
s={1,2,3,4}
print(len(s))

# q.6 check element exist or not 
s={1,2,3,4}
if 3 in s:
    print("element exist")
else:
    print("not element exist")   

# q.7 clear set
s={1,2,3}
s.clear()
print(s)  

# q.8 remove duplicate from list
l=[1,2,3,4,5,5,6,7,7]
s=set(l)
print(s)

# q.9 empty set correctly
s=set()
print(s)

# q.10 union of two sets
a={1,2,3}
b={3,4,5}
print(a.union(b))

# q.11 set and print each element
s={1,2,3,4}
for i in s:
    print(i)

# q.12 intersection
s={1,2,3,4}
v={3,4,5,6}
print(s.intersection(v))

# q.13 differnce between two sets
s={1,2,3}
v={2,3,4}
print(s-v)

# q.14symmetric diffrence
s={1,2,3}
v={2,3,4}
print(s.symmetric_difference(v))

# q.15 subset check
s={1,2}
v={1,2,3}
print(s.issubset(v))

# q.16 superset check
s={1,2,3}
v={2,3,4}
print(s.issuperset(v))

# q.17 disjoint sets
s={1,2}
v={3,4}
print(s.isdisjoint(v))

# q.18 update set
s={1,2}
v={3,4}
s.update(v)
print(s)

# q.19remove random element
s={1,2,3}
s.pop()
print(s)

# q.20 commomn elements in 3 sets
a={1,2,3}
b={2,3,4}
c={3,4,5}
print(a&b&c)

# q.21 find unique character
s='hello world'
unique=set(s)
print(s)

# q.22paragragh uniqe
para='python is easy python is powerfull'
words=para.split()
unique=set(words)
print(len(unique))

# q.23 two list k coomon unique elements
l1=[1,2,3,4]
l2=[3,4,5,6]
common=set(l1)&set(l2)
print(list(common))

# q.24 same nhi h
a={1,2,3}
b={3,4,5}
print(a^b)

# q.25 list m duplicate find kro
l=[1,2,2,3,4,1,5,6,1]
duplicate=[]
for i in l:
    if i not in duplicate:
        duplicate.append(i)
print(duplicate)  

# q.26angram
s1='listen'
s2='silent'
print(set(s1)==set(s2))

# q.27 set se even remove kro
s={1,2,3,4,5,6}
result={i for i in s if i % 2!=0}
print(result)

# q.28 set comprehension(1-10 square)
s={i**2 for i in range(1,11)}
print(s)

# q.29 set m se no>10
s={5,10,15,20,3}
result={i for i in s if i >10}
print(result)

# q.30 multiple sets ka intersection
sets=[{1,2,3,4},{2,3,5},{2,3,6}]
common=set.intersection(*sets)
print(common)








    

