Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def counter():
    x = 0
    while True:
        x += 1
        return x

    
counter()
1
counter()
1
counter()
1
def counter(x):
    while True:
        x += 1
        return x

    
counter(0)
1
counter(x)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    counter(x)
NameError: name 'x' is not defined
def counter():
    x = 0
    while True:
        x += 1
        return x

    
counter()
1
counter()
1
def counter():
    x = 0
    while True:
        x += 1
        yield x

        
counter()
<generator object counter at 0x0000015FEEB8DD90>
count = counter()
next(count)
1
next(count)
2
next(count)
3
next(count)
4
