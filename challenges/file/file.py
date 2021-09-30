#Options: w(write), r(read), a(append), b(binary)
#The option "w" will create or overwrite your file
#The option "a" will append new values in the current file
my_file = open("word.txt", "w")
my_file.write("Batman\n")
my_file.close()#Remember to close the connection because of the operating system