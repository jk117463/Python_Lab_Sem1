# Conditions
p = True
q = True

#Truth Table
if p and q:
    print('p and q')
else:
    print('not p and q')

if p or q:
    print('p or q')
else:
    print('not p or q')

#NAND
if not(p and q):
    print('p and q')
else:
    print('not p and q')

#XOR - Only TRUE when both variables are having DIFFERENT values
if p ^ q:
    print('p XOR q')
else:
    print('not p XOR q')

#pythonic one liners

v = 10 if p else 20
print(v)

# Loops

#For Loop
# i starts from 0 till 7
for i in range(8):
    print(i)

# i starts from 3 till 7
for i in range(3, 7):
    print(i)

# Stopping and breaking

for i in range(8):
    if i==2:
        continue
    if i==6:
        break
    print(i)


#debugging - Using Debug option
# Evaluate expression