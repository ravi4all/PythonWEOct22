Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x = 12
type(x)
<class 'int'>
x = 21312312312312312312312312
type(x)
<class 'int'>
x = 45.23
type(x)
<class 'float'>
x = 3i + 6
SyntaxError: invalid decimal literal
x = 3 + 6i
SyntaxError: invalid decimal literal
x = 3 + i6
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    x = 3 + i6
NameError: name 'i6' is not defined. Did you mean: 'id'?
x = 3 + 6j
type(x)
<class 'complex'>
text = "hello"
text = 'hello'
text = """hello"""
text = '''hello'''
first name = "Ravi"
SyntaxError: invalid syntax
first-name = "Ravi"
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
first_name = "Ravi"
firstName = "Ravi"
@firstName = "Ravi"
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
name = "Ravi"
name.encode()
b'Ravi'
name = b"Ravi"
type(name)
<class 'bytes'>
name
b'Ravi'
text = "नमस्ते आप कैसे हैं ?"
text.encode()
b'\xe0\xa4\xa8\xe0\xa4\xae\xe0\xa4\xb8\xe0\xa5\x8d\xe0\xa4\xa4\xe0\xa5\x87 \xe0\xa4\x86\xe0\xa4\xaa \xe0\xa4\x95\xe0\xa5\x88\xe0\xa4\xb8\xe0\xa5\x87 \xe0\xa4\xb9\xe0\xa5\x88\xe0\xa4\x82 ?'
text = text.encode()
text
b'\xe0\xa4\xa8\xe0\xa4\xae\xe0\xa4\xb8\xe0\xa5\x8d\xe0\xa4\xa4\xe0\xa5\x87 \xe0\xa4\x86\xe0\xa4\xaa \xe0\xa4\x95\xe0\xa5\x88\xe0\xa4\xb8\xe0\xa5\x87 \xe0\xa4\xb9\xe0\xa5\x88\xe0\xa4\x82 ?'
text.decode()
'नमस्ते आप कैसे हैं ?'
text = "234"
text.encode()
b'234'
num = 232
num = b232
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    num = b232
NameError: name 'b232' is not defined
num = b'232'
num
b'232'
game = True
game = Frue
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    game = Frue
NameError: name 'Frue' is not defined. Did you mean: 'True'?
game = False
type(game)
<class 'bool'>
game = true
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    game = true
NameError: name 'true' is not defined. Did you mean: 'True'?
True = 34
SyntaxError: cannot assign to True
marks = [45,78,36,82,78]
type(marks)
<class 'list'>
marks = (45,78,36,82,78)
type(marks)
<class 'tuple'>
marks = {"phy" : 45, "chem" : 78, "math" : 36, "eng" : 77}
marks
{'phy': 45, 'chem': 78, 'math': 36, 'eng': 77}
type(marks)
<class 'dict'>
x = {4,3,4,6,8,9,23,34,4,5,7,9,909,9,56,3,2}
x
{34, 3, 4, 5, 6, 7, 8, 9, 2, 909, 23, 56}
x
{34, 3, 4, 5, 6, 7, 8, 9, 2, 909, 23, 56}
x
{34, 3, 4, 5, 6, 7, 8, 9, 2, 909, 23, 56}
marks = [45,78,36,82,78]
marks[0]
45
marks[1]
78
marks[2]
36
