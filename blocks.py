# Indentation defines BLOCK of code in python
for i in range(8):
    if i==2:
        continue
    if i==6:
        break
print(i) # Prints the data after the loop runs
print('*********************************')

# Indentation defines BLOCK of code in python
for i in range(8):
    if i==2:
        continue
    if i==6:
        break
    print(i) # Print is part of loop(not under any condition of loop)

print('*********************************')

# For loop has to run at least once to see b or make b visible
a =10
for i in range(3):
    print(i)
    print(a)
    b=15

print('b=%s' % b)

print('*********************************')
if a>5:
    if b>5:
        c = 10
else:
    c =50
print('c=%s' % c)

#Blocks with functions

def sum(a,b):
    print('a=%s' % a)
    print('b=%s' % b)
    a =100
    return a + b

a = 10
b = 20
print("Sum = %s" % sum(a,b))
print('a=%s' % a) # Definition of a in side a function doesn't change value in the main execution


# homework List the prime numbers
# Due in 2 weeks
