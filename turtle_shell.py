Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> t = turtle.Pen()
>>> t.shape("turtle")
>>> t.forward(200)
>>> t.left(90)
>>> t.forward(200)
>>> t.left(90)
>>> t.forward(200)
>>> t.left(90)
>>> t.forward(200)
>>> t.left(90)
>>> for i in range(5):
...     print(i)

    
0
1
2
3
4
for i in range(2,8):
    print(i)

    
2
3
4
5
6
7
t.reset()
for i in range(4):
    t.forward(200)
    t.left(90)

    
t.reset()
for i in range(60):
    t.forward(3*i)
    t.left(45)

    
t.reset()
i = 0
while i < 60:
    t.forward(200)
    t.left(90)
    i += 1

    
t.reset()
