Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
text = "hello how are you"
len(text)
17
text[0]
'h'
text[-1]
'u'
text[6]
'h'
text[17]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    text[17]
IndexError: string index out of range
text[0] = 'b'
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    text[0] = 'b'
TypeError: 'str' object does not support item assignment
del text[0]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    del text[0]
TypeError: 'str' object doesn't support item deletion
text
'hello how are you'
text[0:4]
'hell'
text[4:15]
'o how are y'
text[0:]
'hello how are you'
text[10:]
'are you'
text[:10]
'hello how '
text[:]
'hello how are you'
text[0:15]
'hello how are y'
text[0:15:1]
'hello how are y'
text[0:15:2]
'hlohwaey'
text[0:15:3]
'hlh e'
text[10:0]
''
text[10:0:-1]
'a woh olle'
text[10::-1]
'a woh olleh'
text[::-1]
'uoy era woh olleh'
text[-1:-10]
''
text[-1:-10:-1]
'uoy era w'
dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
