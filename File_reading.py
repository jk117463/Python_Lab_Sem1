file_path= 'test.txt'

my_file = open(file_path, 'r')
lines = my_file.readlines()
i=1
for line in lines:
    print('{}: {}'.format(i,line), end='')
    i+=1
my_file.close()

file_path= 'test.csv'

my_file = open(file_path, 'r')
lines = my_file.readlines()
i=1
for line in lines:
    print(type(line))
    print('{}: {}'.format(float,line), end='')
    i+=1
my_file.close()