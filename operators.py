Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x = 12
y = 23
x + y
35
x - y
-11
x / y
0.5217391304347826
x * y
276
18 / 6
3.0
18 / 5
3.6
18 / 7
2.5714285714285716
18 // 7
2
18 // 5
3
12 * 5
60
12 ** 5
248832
2 ** 2
4
2 ** 3
8
2 ** 4
16
2 ** 5
32
45 / 5
9.0
45 % 5
0
45 % 7
3
45 % 8
5
round(4.5)
4
round(4.6)
5
round(4.4)
4
import math
math.floor(4.6)
4
math.floor(4.8)
4
math.floor(4.3)
4
math.ceil(4.3)
5
math.ceil(4.8)
5
math.ceil(-4.8)
-4
math.ceil(-4.2)
-4
math.floor(-4.3)
-5
math.floor(-4.8)
-5
x = 10
x + 5
15
x
10
x = x + 5
x
15
x += 5
x
20
x *= 4
x
80
x **= 2
x
6400
12 > 7
True
12 < 7
False
12 > 12
False
12 >= 12
True
12 == 12
True
12 != 12
False
12 % 2
0
12 % 2 == 0
True
17 % 5 == 0
False
text = "Hello Ram How are you..?"
"Hello" in text
True
"hello" in text
False
data = [3,45,6,2,5,8,13]
10 in data
False
45 in data
True
x = 12
y = x
z = 12
x == y
True
x is y
True
x is z
True
x = [3,4,5]
y = x
x == y
True
x is y
True
x = "Hello World this is Python"
y = "Hello World this is Python"
x == y
True
x is y
False
id(12)
2611573490256
x = 12
y = x
z = 12
id(x)
2611573490256
id(y)
2611573490256
id(z)
2611573490256
id(12)
2611573490256
x = "Hello World this is Python"
y = "Hello World this is Python"
id(x)
2611610418464
id(y)
2611610418864
x is y
False
x = "hello"
y = "hello"
x is y
True
x = "hello world"
y = "hello world"
x is y
False
x = 1
x += 1
x
2
12 & 5
4
