# 1. Count Character Frequency
s = "banana"
d = {}

for i in s:
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1

print(d)

# 2. Merge Two Dictionary
d1 = {'a':10, 'b':20}
d2 = {'b':5, 'c':15}

for i in d2:
    if i in d1:
        d1[i] = d1[i] + d2[i]
    else:
        d1[i] = d2[i]

print(d1)

# 3. Group Words by First Letter
words = ['apple','ant','banana','ball']
d = {}

for w in words:
    first = w[0]

    if first not in d:
        d[first] = []

    d[first].append(w)

print(d)

# 4. Even Odd Dictionary
nums = [1,2,3,4,5]

d = {'even':[], 'odd':[]}

for n in nums:
    if n % 2 == 0:
        d['even'].append(n)
    else:
        d['odd'].append(n)

print(d)

# 5. Check Unique Values
d = {'a':1,'b':2,'c':3}

values = list(d.values())

if len(values) == len(set(values)):
    print("True")
else:
    print("False")

# 6. Valid Parenthesis
s = "()[]{}"
stack = []

for i in s:
    if i in "([{":
        stack.append(i)
    else:
        stack.pop()

if len(stack) == 0:
    print("Valid")
else:
    print("Not Valid")

    

