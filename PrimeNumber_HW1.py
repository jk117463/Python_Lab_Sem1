print("Enter the Limit untill which Prime numbers needs to be listed")
limit = int(input())

print(limit)

i = 1
ind = 0
j = 1
for i in range(i, limit):
    for j in range (i, int(i/2)):
        if i%j == 0:
            ind = 1
            break
    if ind == 1:
        print(i)