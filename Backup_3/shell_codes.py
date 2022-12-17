Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import datetime
datetime.datetime.now()
datetime.datetime(2022, 12, 17, 16, 9, 27, 684573)
datetime.datetime.now().date
<built-in method date of datetime.datetime object at 0x0000017C5A74A790>
from datetime import datetime as dt
d = dt.now().date()
t = dt.now().time()
print(d)
2022-12-17
print(t)
16:10:51.114202
d.strftime("%d/%m/%y")
'17/12/22'
d.strftime("%d-%m-%y")
'17-12-22'
d.strftime("%d-%m-%Y")
'17-12-2022'
d.strftime("%D-%m-%Y")
'12/17/22-12-2022'
d.strftime("%D")
'12/17/22'
d.strftime("%d-%M-%Y")
'17-00-2022'
d.strftime("%d-%q-%Y")
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    d.strftime("%d-%q-%Y")
ValueError: Invalid format string
d.strftime("%d-%x-%Y")
'17-12/17/22-2022'
d.strftime("%d-%b-%Y")
'17-Dec-2022'
d.strftime("%d-%B-%Y")
'17-December-2022'
d.strftime("%d-%B-%Y, %a")
'17-December-2022, Sat'
d.strftime("%d-%B-%Y, %A")
'17-December-2022, Saturday'
t.strftime("%H:%M:%S")
'16:10:51'
t.strftime("%I:%M:%S")
'04:10:51'
t.strftime("%I:%M:%S, %p")
'04:10:51, PM'
t.strftime("%I:%M:%S, %P")
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    t.strftime("%I:%M:%S, %P")
ValueError: Invalid format string
random.randint(1,100)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    random.randint(1,100)
NameError: name 'random' is not defined
import random
random.randint(1,100)
74
print("hello")
hello
import os
os.listdir()
['DLLs', 'Doc', 'etc', 'include', 'Lib', 'libs', 'LICENSE.txt', 'NEWS.txt', 'python.exe', 'python3.dll', 'python310.dll', 'pythonw.exe', 'Scripts', 'share', 'tcl', 'Tools', 'vcruntime140.dll', 'vcruntime140_1.dll']
os.getcwd()
'C:\\Python310'
os.chdir("D:\Batches\Songs\new_songs")
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    os.chdir("D:\Batches\Songs\new_songs")
OSError: [WinError 123] The filename, directory name, or volume label syntax is incorrect: 'D:\\Batches\\Songs\new_songs'
os.chdir(r"D:\Batches\Songs\new_songs")
#r - raw string
os.getcwd()
'D:\\Batches\\Songs\\new_songs'
os.listdir()
['471551_RlI2lBF7EevSIYjva7WRBw.png', 'bang-bang.mp3', 'DBSCAN_tutorial.gif', 'Faded.mp3', 'FadedCopy.mp3']
import glob
glob.glob("*.mp3")
['bang-bang.mp3', 'Faded.mp3', 'FadedCopy.mp3']
somgs = glob.glob("*.mp3")
songs = glob.glob("*.mp3")
songs
['bang-bang.mp3', 'Faded.mp3', 'FadedCopy.mp3']
import random
random.choice(songs)
'FadedCopy.mp3'
random.choice(songs)
'bang-bang.mp3'
random.choice(songs)
'FadedCopy.mp3'
random.choice(songs)
'Faded.mp3'
os.startfile(random.choice(songs))
os.startfile(random.choice(songs))
os.startfile(random.choice(songs))
