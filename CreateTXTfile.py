#  Creates txt files with default data
for i in range(1, 101):  # Range
    fn = "A" + f"{i:04d}" + ".txt"  # set Filename
    print(fn)
    pn = "C:\\Users\\jathi\\PycharmProjects\\Python_Lab_Sem1\\CC\\homework2\\" + fn  # Set Pathname depends on ur system
    fh = open(pn, 'w')  # Create file and open
    fh.write("jk117463")  # Write student id to created file
    fh.close()  # Close file


