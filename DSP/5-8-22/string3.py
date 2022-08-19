Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #endswith():
>>> str="santhoshi"
>>> print(str.endswith("c"))
False
>>> print(str.endswith("i"))
True
>>> print(str.endswith("hi"))
True
>>> print(str.endswith("hoshi"))
True
>>> print(str.endswith("hs"))
False
>>> print(str.endswith("samthoshi"))
False
>>> print(str.endswith("santhoshi"))
True
>>> #lower():
>>> str="CHanti"
>>> print(str.lower())
chanti
>>> #isalnum():
>>> str="rgukt123"
>>> print(str.isalnum())
True
>>> str="rgukt 123"
>>> print(Str.isalnum())
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print(Str.isalnum())
NameError: name 'Str' is not defined
>>> print(str.isalnum())
False
>>> str="123 rgukt"
>>> print(str.isalnum())
False
>>> #isalpha():
>>> str="chanti"
>>> print(str.isalpha())
True
>>> str="123dufh"
>>> print(Str.isalpha())
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print(Str.isalpha())
NameError: name 'Str' is not defined
>>> print
<built-in function print>
>>> print(str.isalpha())
False
>>> str="2342"
>>> print(str.isalpha())
False
>>> 