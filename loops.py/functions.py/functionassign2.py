print("q1")
li = [1,2,3,4]
def sq (x):
    return x**2
print(tuple(map(sq,li)))

print("q2")
celisus=[1,10,20,40]
#using map with lambda function
fahrenheit=list(map(lambda c:(c* 9/5)+32,celisus)) #this is easy bcz this is one line code
print(fahrenheit)

#using only map
celisus=[1,10,20,40]
def fahrenheit (c):
    return(c* 9/5)+32
result=map(fahrenheit,celisus)
print(list(result))

print("q3")
s = ["sanjana sarthak", "Hello i am sarthak jain"]
result=list(map(str.upper,s))
print(result)

print("q4")
#print len of str
def length(words):
    return len(words)
words = ["sanjana sarthak", "Hello i am sarthak jain"]
result = list(map(length, words))
print(result)


print("q5")
#change space into A
s = ["sanjana sarthak", "Hello i am sarthak jain"]

def change_space(x):
    return x.replace(" ", "a")

result = list(map(change_space, s))

print(result)

print("q6")
#Given a list of numbers, use map with a lambda function to add 10 to each element and print the updated list.
li=[1,2,3,4,5]
result=list(map(lambda x:x+10,li))
print(result)

#without using lambda
li=[1,2,3,4,5]
def add10(x):
    return x + 10
result=list(map(add10,li))
print(result)