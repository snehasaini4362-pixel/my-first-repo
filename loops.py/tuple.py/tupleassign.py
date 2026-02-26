# 1.Create a tuple containing five different numbers and display it
t=(10,20,30,40,50)
print(t)

# 2. Access the first and last element of a tuple
t=(10,20,30,40,50)
print("first",t[0])
print("second",t[-1])

# 3.Find the total number of elements present in a tuple
t=(10,20,30,40,50)
print("total element present",len(t))

# 4. Check whether a given value exists inside a tuple
t=(10,20,30,40,50)
value=30
if value in t:
    print("value exist")
else:
    print("not exist")    

# 5.Concatenate two tuples and print the new tuple 
t1=(1,2,3)
t2=(4,5,6)
new_tuple=t1+t2
print(new_tuple)   

# 6. Repeat a tuple two times using an operator
t=(1,2)
print(t*2)

# 7 Find the index of a specific element in a tuple
t=(10,20,30,40,50)
print("index of 30:",t.index(30))

# 8 Count how many times a particular value appears in a tuple
t=(1,2,3,2,4,2)
print(t.count(2))

# 9.Slice a tuple to display elements from index 1 to 4
t=(0,1,2,3,4,5,6)
print(t[1:5])

# 10. Iterate through all elements of a tuple using a loop
t=(10,20,30,40,50)
for i in t:
    print(i)