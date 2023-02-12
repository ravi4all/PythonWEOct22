import io

try:
    file = open('file_1.txt','w')
    data = "hello"
    file.write(data)
    data = file.read()
    print(data)
except io.UnsupportedOperation:
    print("Operation not supported...")
finally:
    file.close()
    print("File Closed...")