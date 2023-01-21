Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def sayHello():print("Hello User")

def sayBye():print("Bye User")

greet = [sayHello(), sayBye()]
Hello User
Bye User
greet
[None, None]
greet = [sayHello, sayBye]
greet
[<function sayHello at 0x00000200F17C7760>, <function sayBye at 0x00000200F17C4700>]
greet[0]
<function sayHello at 0x00000200F17C7760>
greet[0]()
Hello User
greet[1]()
Bye User
numbers = [4,2,12,5,8,2,7]
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        print(numbers[i])

        
4
2
12
8
2
def even(n):
    return n % 2 == 0

filter(even, numbers)
<filter object at 0x00000200F179F100>
list(filter(even, numbers))
[4, 2, 12, 8, 2]
lambda x,y : x + y
<function <lambda> at 0x00000200F17C7880>
(lambda x,y : x + y)(3,4)
7
list(filter(lambda n : n % 2 == 0, numbers))
[4, 2, 12, 8, 2]
def add(x,y):
    return x + y

list(map(lambda n : n * 10, numbers))
[40, 20, 120, 50, 80, 20, 70]
#Decorators
