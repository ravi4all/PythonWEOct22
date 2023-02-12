# it will create a new file if file doesn't exists
# file = open("file_1.txt", "w")
# it will overwrite the file if file already exists
# file.write("File Handling Using Python...")
# file.close()

# append - if we want to append data
# file = open("file_1.txt", "a")
# file.write("\nThis is new data")
# file.close()

# x mode - it will write the file
# it will always create a new file
# if file already exists then it won't get executed
file = open("file_1.txt", "x")
file.write("File Handling Using Python...")
file.close()
