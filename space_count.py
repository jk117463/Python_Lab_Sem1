import os
my_dir = 'C:\\Datascience\\Temp'

def sum_space(folder):
    sum = 0
    for f in os.listdir(folder):
        if os.path.isfile(os.path.join(folder, f)):
            size = os.path.getsize(os.path.join(folder, f))
            sum = sum + size
        else:
            sum = sum + sum_space(os.path.join(folder, f))
    return sum

print('Space occupied by {}: {}'.format(my_dir, sum_space(my_dir)))

