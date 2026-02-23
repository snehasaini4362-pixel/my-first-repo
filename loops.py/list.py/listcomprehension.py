# list comrehension = is a concised way to generate a list by using for loop and some condition 
# syntax=[expresion for exp]
#  num=[i for i in range(1,101)if i%2!=0]
# print(num)

# num=[i*i for i in range(1,10)]
# print(num)

# li = ['apple','car','elephant','dog','cat']
# li=[i for i in li if len(i)<4]
# print(li)

# li = [1,2,3,4,5,6,7,8,10,12,15]
# li=[i for i in li if i>10]
# print(li)


#                                   basic practice

# qq.1
# print 10 no.in list using com.
num=[i for i in range(1,11)]
print(num)

# qq.2 print 1 to 10 square no.
num=[i*i for i in range(10)]
print(num)

# qq.3 cube 1to10
num=[i**3 for i in range(1,10)]
print(num)

# qq.4
num=[i for i in range(1,20)if i%2==0]
print(num)

# qq.5
num=[i for i in range(1,20)if i % 2!=0]
print(num)

#                                   using conditions
# qq.1 divisble by 3 from 1 to 30
num=[i for i in range(1,31)if i % 3==0]
print(num)


# qq.2 greater than 10
li=[[1,2,3],[4,5,6],[7,8,9]]
greater=[j for i in li for j in i if j>10]
print(greater)

# qq.3 print a list only positive no.
li=[[1,2,3],[4,-5,6],[7,-8,9]]
positive=[j for i in li for j in i if j>0]
print(positive)

# qq.4 print a list only negetive no.
li=[[1,2,3],[4,-5,6],[7,-8,9]]
negetive=[j for i in li for j in i if j<0]
print(negetive)

# qq.5 print a list square is greater than 50
square=[i for i in range(1,11)if i*i>50]
print(square)


#                             working with strings

# qq.1 convert words a list into uppercase
words=["apple","banana","cherry"]
upper=[i.upper() for i in words]
print(upper)

# qq.2 convert into lower case
words=["apple","banana","cherry"]
upper=[i.lower() for i in words]
print(upper)

# qq.3 lenth of each word
words=["apple","banana","cherry"]
lengths=[len(i) for i in words]
print(lengths)

# qq.4
# words with more than 4 characters
word=["apple","banana","cherry"]
long_words=[i for i in words if len(word)> 4]
print(long_words)


#            nestedlist comprehension

li=[[1,2,3],[4,5,6],[7,8,9]]
num=[j for i in li for j in i if j % 2==0]
print(num)

li=[[1,2,3],[4,5,6],[7,8,9]]
num=[[i**2 for i in j]for j in li]
print(num)

words=["apple","sky","orange","try","banana"]
vowel=[i for i in words if sum(1 for ch in i if ch in "aeiou")>=2]
print(vowel)

num=[i**2 if i%2==0 else i**3 for i in range(1,21)]
print(num)

li=[[10,20],[30,40],[50,60]]
flat=[j for i in li for j in i]
print(flat)


#                            important qq.
data=[10, None ,25, None ,40,0,55]
cleaned=[i for i in data if i is not None]
print(cleaned)






