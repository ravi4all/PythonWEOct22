Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
data = {}
type(data)
<class 'dict'>
data = dict()
type(data)
<class 'dict'>
data = {"name":"John","dept":"IT"}
data.keys()
dict_keys(['name', 'dept'])
data.values()
dict_values(['John', 'IT'])
data.items()
dict_items([('name', 'John'), ('dept', 'IT')])
data[0]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    data[0]
KeyError: 0
data["name"]
'John'
data["dept"]
'IT'
data["salary"] = 45000
data
{'name': 'John', 'dept': 'IT', 'salary': 45000}
data.fromkeys(["name","dept"])
{'name': None, 'dept': None}
data.get("name")
'John'
data["name"]
'John'
data["phone"]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    data["phone"]
KeyError: 'phone'
data.get("phone")
data.get("phone", "Not Available")
'Not Available'
data.get("name", "Not Available")
'John'
data.get("address", "Not Available")
'Not Available'
data.pop('dept')
'IT'
data
{'name': 'John', 'salary': 45000}
data.popitem()
('salary', 45000)
data
{'name': 'John'}
data.setdefault('dept')
data
{'name': 'John', 'dept': None}
data['dept'] = 'IT'
data
{'name': 'John', 'dept': 'IT'}
details = {'address' : 'Delhi', 'phone' : 987654346}
data + details
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    data + details
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
data.update(details)
data
{'name': 'John', 'dept': 'IT', 'address': 'Delhi', 'phone': 987654346}
data = {i : i ** 2 for i in range(1,11)}
data
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
data = {'name': 'John', 'dept': 'IT', 'address': 'Delhi', 'phone': 987654346}
for key in data:
    print(key)

    
name
dept
address
phone
for key in data:
    print(key, ":", data[key])

    
name : John
dept : IT
address : Delhi
phone : 987654346



# sets
x = {4,65,2,5,8,8,1,3,7,8,23,67,9,2}
x
{65, 2, 1, 4, 5, 3, 7, 8, 67, 9, 23}
y = {1,2,3,4,5,6,7,2,3,1,4,6,67,2,7,9,1}
y
{1, 2, 3, 4, 5, 6, 7, 67, 9}
x & y
{1, 2, 3, 4, 5, 67, 7, 9}
x | y
{65, 2, 1, 4, 5, 3, 7, 8, 67, 9, 6, 23}
x - y
{8, 65, 23}
x.intersection(y)
{1, 2, 3, 4, 5, 67, 7, 9}
x.union(y)
{65, 2, 1, 4, 5, 3, 7, 8, 67, 9, 6, 23}
x.difference(y)
{8, 65, 23}
