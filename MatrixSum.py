
#sum up matrix
l2d = [[5,5,7],
        [4,5,6],
        [7,8,9]]
print(l2d[1][1])
#Sum up rows
#sum all elements
total = 0
r = 1
for i in l2d:
    sum = 0
    print(i)
    for i1 in i:
        if (type(i1) == int or type(i1) == float):
          sum=sum + i1
    print('Sum of row {}'.format(r), sum)
    r = r + 1
    total = total + sum
print('Sum of all rows {}'.format(total))

# #Sum up columns
l2d = [[5,5,7],
        [4,5,6],
        [7,8,9]]
print(l2d[1][1])
colsum = []
for i in range(len(l2d[0])):
    sum = 0
    for j in range(len(l2d)):
          sum=sum + l2d[j][i]
    print('Sum of column {}'.format(i+1), (sum))
    colsum.append(sum)
print(colsum)

#Using numpy
import Numpy as np
s_cols = np.sum(l2d, axis = 0)
print(s_cols)
s_rows = np.sum(l2d, axis = 1)
print(s_rows)
