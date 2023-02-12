file = open("file_data.txt", "r")
# data = file.read()

# data = file.readline()
# data = file.readlines()

data = file.read(5)
print(data)
file.close()
