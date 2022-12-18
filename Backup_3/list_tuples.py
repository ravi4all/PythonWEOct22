Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
dtaa = [4,2,6,2,9,12,'hello',45.23,True]
data = [4,2,6,2,9,12,'hello',45.23,True]
data = []
data.append(34)
dara
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    dara
NameError: name 'dara' is not defined. Did you mean: 'data'?
data
[34]
data.append(45)
data
[34, 45]
data.append(45,67,33,90)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    data.append(45,67,33,90)
TypeError: list.append() takes exactly one argument (4 given)
data.append([45,67,33,90])
data
[34, 45, [45, 67, 33, 90]]
data[-1]
[45, 67, 33, 90]
del data[-1]
data
[34, 45]
data.extend([45,67,33,90])
data
[34, 45, 45, 67, 33, 90]
data[-1]
90
data.insert(2,16)
data
[34, 45, 16, 45, 67, 33, 90]
data.pop()
90
data
[34, 45, 16, 45, 67, 33]
data.pop(1)
45
data
[34, 16, 45, 67, 33]
data.remove(2)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    data.remove(2)
ValueError: list.remove(x): x not in list
data.sort()
data
[16, 33, 34, 45, 67]
data.sort(reverse=True)
data
[67, 45, 34, 33, 16]
data
[67, 45, 34, 33, 16]
for i in range(len(data)):
    print(data[i])

    
67
45
34
33
16
for i in range(len(data)):
    print(i, "-", data[i])

    
0 - 67
1 - 45
2 - 34
3 - 33
4 - 16
for i in data:
    print(i)

    
67
45
34
33
16
data = []
for i in range(1,11):
    data.append(i)

    
data
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data = [i for i in range(1,11)]
data
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data = [i**2 for i in range(1,11)]
data
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
data = [i for i in range(1,11) if i % 2 == 0]
data
[2, 4, 6, 8, 10]
data = [["John","Sam","Mac"],[45000,56000,35000],["IT", "HR", "IT"]]
data
[['John', 'Sam', 'Mac'], [45000, 56000, 35000], ['IT', 'HR', 'IT']]
data[0]
['John', 'Sam', 'Mac']
data[0][0]
'John'
data[1][0]
45000
data[2][0]
'IT'
for i in range(len(data)):
    print(data[0][i], data[1][i], data[2][i])

    
John 45000 IT
Sam 56000 HR
Mac 35000 IT
x = (3,2,4,1,4)
del x[0]
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    del x[0]
TypeError: 'tuple' object doesn't support item deletion
