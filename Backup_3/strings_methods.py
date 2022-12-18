Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
text = "Hello how are you..?"
dir(text)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
text.lower()
'hello how are you..?'
text.upper()
'HELLO HOW ARE YOU..?'
text.capitalize()
'Hello how are you..?'
text.title()
'Hello How Are You..?'
text.swapcase()
'hELLO HOW ARE YOU..?'
text.count('h')
1
text.count('o')
3
text.index('o')
4
text.index('o',0)
4
text.index('o',5)
7
text.index('o',8)
15
text.index('o',16)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    text.index('o',16)
ValueError: substring not found
text.find('o')
4
text.find('o',5)
7
text.find('o',8)
15
text.find('o',16)
-1
text.index('z')
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    text.index('z')
ValueError: substring not found
text.find('z')
-1
count = text.count('o')
count
3
index = 0
for i in range(count):
    index = text.find('o', index)
    index += 1

    
for i in range(count):
    index = text.find('o', index)
    print(index)
    index += 1

    
-1
4
7
index = 0
for i in range(count):
    index = text.find('o', index)
    print(index)
    index += 1

    
4
7
15
text.rfind('o')
15
text.rindex('o')
15
text.split()
['Hello', 'how', 'are', 'you..?']
data = "Ram,40,IT,45000"
data.split()
['Ram,40,IT,45000']
data.split(",")
['Ram', '40', 'IT', '45000']
x = data.split(",")
x
['Ram', '40', 'IT', '45000']
" ".join(x)
'Ram 40 IT 45000'
",".join(x)
'Ram,40,IT,45000'
text = "   Hello World    "
text.strip()
'Hello World'
text.lstrip()
'Hello World    '
text.rstrip()
'   Hello World'
text = text.strip()
text
'Hello World'
text = "###Hello World$$$"
text.strip()
'###Hello World$$$'
text.lstrip("#")
'Hello World$$$'
text = text.lstrip("#")
text
'Hello World$$$'
text = text.rstrip("$")
text
'Hello World'
text.startswith('h')
False
text.startswith('H')
True
text.endswith()
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    text.endswith()
TypeError: endswith() takes at least 1 argument (0 given)

text.endswith('?')
False
text.isupper()
False
text.islower()
False
text.isalpha()
False
text.isprintable()
True
text.isdigit()
False
len(text)
11
text.zfill(10,text)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    text.zfill(10,text)
TypeError: str.zfill() takes exactly one argument (2 given)
text.zfill(10)
'Hello World'
text.zfill(11)
'Hello World'
text.zfill(12)
'0Hello World'
text.zfill(13)
'00Hello World'
text.zfill(20)
'000000000Hello World'
