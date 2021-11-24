file_path= 'test.txt'

with open(file_path, 'r') as my_file:
    lines = my_file.readlines()
    i=0
    for line in lines
        print('{}: {}'.format(i,line), end='')
        i+=1