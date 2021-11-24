l1 = [4232, 245326, 57467347, 362363]

print(l1[0])
print(l1[3])
print(l1[-1])

l2 = l1[1:4]
print(l2)
l2.append(45454)
print(l2)
l2.insert(2, 333)
l2[1] = 44
print(l2)

# sorting
l3=l2
l3.sort()
print(l3)

#Find Python word
l4 = [3636, 78785, 1526, 255.453, 'Hello Python 3', 45456]
print(l4[4][6:12]) #direct print
word = l4[4]
print(word)
res = word.split()
print(res)
print(res[1])

l4 = [1, 2, 3, 3, 'Hello Python 3', 1]

#Sum all number values of l4
sum = 0
print(l4)
for i in l4:
    if (type(i) == int or type(i) == float):
    #if (isinstance(i,int) or isinstance(i,float)):
        sum=sum + i
print(sum)

l5 = sum([i for i in l4 if (type(i) == int or type(i) == float)])
print(l5)

