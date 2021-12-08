import os
#current working directory
in_path = os.path.join(os.getcwd(),'.keep')
print(in_path)

#to print current files path - prints fwd slash like in windows
print(__file__)

my_file_path = __file__
my_parent_dir = os.path.dirname(my_file_path)
my_file_name = os.path.basename(my_file_path)
print(my_parent_dir)
print(my_file_name)

#listing files in current wd
print(os.listdir(my_parent_dir))

#list files in a path
print(os.listdir("C:\\Users"))

#print each file or directory in
my_dir= 'C:\\Users\\jathi'
for f in os.listdir(my_dir):
    type = 'd' if os.path.isdir(os.path.join(my_dir, f)) else '-'
    size = os.path.getsize(os.path.join(my_dir, f))
    print('{} {} {}'.format(type, size, f))
    print(f)