file = open("word.txt", "r")
file_content = file.read()
print(f"file_content:\n{file_content}")

#This time nothing will be returned, because the pointer stopped in the last line of the file,
#because of the first "file.read()"
file_content = file.read()
print(f"file_content:\n{file_content}")

file.close()