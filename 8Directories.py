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