Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

========== RESTART: D:\Batches\2022\PythonOctWE\BackUp\taking_input.py =========
Enter your name : Ravi
Hello : Ravi
Enter first number : 12
Enter second number : 33
Sum is 45
x = 12
x = 1221312312312312
x = 122131231231231234324214324
type(x)
<class 'int'>
import sys
x = 0
sys.getsizeof(x)
24
x = 1
sys.getsizeof(x)
28
x = 2
sys.getsizeof(x)
28
sys.getsizeof(12312)
28
sys.getsizeof(12312213123)
32
sys.getsizeof(123122131)
28
sys.getsizeof(1231221312)
32
2 ** 31
2147483648
sys.getsizeof(1231221312121212)
32
sys.getsizeof(1231221312121212233)
36
sys.getsizeof(123122131212121223323431243232234)
40
sys.getsizeof(4.5)
24
sys.getsizeof(14.5)
24
sys.getsizeof(14.53)
24
sys.getsizeof(14213123.3434234253)
24
sys.getsizeof(14213123.34342342532312312312)
24
sys.getsizeof(1421312123123123123.34342342532312312312)
24
name = "Ram Sharma"
sys.getsizeof(name)
59
sys.getsizeof("")
49
sys.getsizeof("a")
50
sys.getsizeof("ab")
51
sys.getsizeof("abc")
52
sys.getsizeof("abcd")
53
name.upper()
'RAM SHARMA'
x = True
type(x)
<class 'bool'>
>>> x = [3,1,2,12,5,7]
>>> type(x)
<class 'list'>
>>> x = (4,32,5,2,5,8)
>>> type(x)
<class 'tuple'>
>>> x = {"name" : "Ram", "age" : 30, "dept" : "IT"}
>>> x
{'name': 'Ram', 'age': 30, 'dept': 'IT'}
>>> x = {3,2,4,7,5,5,9,0,2,3,5,6,2,4,6,8}
>>> x
{0, 2, 3, 4, 5, 6, 7, 8, 9}
>>> y = {13,3,1,4,6,8,23,56,6,23,7,8,4,11}
>>> y
{1, 3, 4, 6, 7, 8, 11, 13, 23, 56}
>>> x = b"hello"
>>> type(x)
<class 'bytes'>
