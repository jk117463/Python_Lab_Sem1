#Count size of a folder including sub-directory
import os
my_dir = 'C:\\Datascience\\Sem 1\\PythonLab\\temp'

def sum_space(folder):
    sum = 0
    for f in os.listdir(folder):
        path = os.path.join(folder, f)
        if os.path.isfile(path):
            size = os.path.getsize(path)
            sum = sum + size
        else:
            sum = sum + sum_space(path) # Call recursively for all sub folders
    return sum

print('Space occupied by {}: {}'.format(my_dir, sum_space(my_dir)))

