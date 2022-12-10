Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
t = turtle.Pen()
t.shape("turtle")
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
num = 5
print(5*1)
5
print(5*2)
10
for i in range(4):
    print(i)

    
0
1
2
3
for i in range(4,8):
    print(i)

    
4
5
6
7
t.reset()
for i in range(4):
    t.forward(200)
    t.left(90)

    
t.reset()
for i in range(40):
    t.forward(3 * i)
    t.left(45)

    
t.reset()
for i in range(4):
    t.forward(200)
    t.left(90)

    
t.reset()
for i in range(30):
    t.circle(5*i)
    t.left(180)

    
t.reset()
t.speed(0)
for i in range(60):
    t.circle(5*i)
    t.left(180)

    
t.reset()
t.speed(0)
for i in range(60):
    t.circle(5*i)
    t.left(45)

    
t.reset()
t.color("red")
t.speed(0)
for i in range(40):
    t.circle(5*i)
    t.left(90)

    
