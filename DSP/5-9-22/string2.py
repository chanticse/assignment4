Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>  #isdecimal():
>>> str="122324"
>>> print(str.isdecimal())
True
>>> str="rgukt123"
>>> print(str.isdecimal())
False
>>> str="rgukt 123"
>>> print(str.isdecimal())
False
>>> str="123 456"
>>> print(str.isdecimal())
False
>>> str="1 2 3 4
SyntaxError: EOL while scanning string literal
>>> str="1 2 3 "
>>> print(str.isdecimal())
False
>>> str="01234"
>>> print(str.isdecimal())
True
>>> #isdigit():
>>> str="34235"
>>> print(str.isdigit())
True
>>> str="rgukt123"
>>> print(str.isdigit())
False
>>> str=
SyntaxError: invalid syntax
>>> str="3"
>>> print(str.isdigit())
True
>>> str="hii how are you"
>>> print(str.islower())
True
>>> str="hii How are You"
>>> print(str.islower())
False
>>> #isupper():
>>> str="HOW ARE YOU"
>>> print(str.isupper())
True
>>> #isspace():
>>> str="  "
>>> print(str.isspace())
True
>>> str="  hii  "
>>> print(str.isspace())
False
>>> a="HELLO AND WELCOME TO MY WORLD"
>>> B="Hello"
>>> c="22 Names"
>>> d="This Is %'!?"
>>> print(a.istitle())
False
>>> print(b.istitle())
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    print(b.istitle())
NameError: name 'b' is not defined
>>> print(B.istitle())
True
>>> print(c.istitle())
True
>>> print(d.istitle())
True
>>> x="chanti chanti cse cse "
>>> print(x.find("cse"))
14
>>> print(x.find("a"))
2
>>> print(x.find("b"))
-1
>>> print(x.find("a",5,8))
-1
>>> print(x.find("a",7,10))
9
>>> a="hello hii"
>>> print(a.index("hii"))
6
>>> print(a.index("0",1,7))
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    print(a.index("0",1,7))
ValueError: substring not found
>>> print(a.index("o",1,7))
4
>>> print(a.index("w"))
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    print(a.index("w"))
ValueError: substring not found
>>> print(a.index("cse" "cse"))
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    print(a.index("cse" "cse"))
ValueError: substring not found
>>> print(x.index("cse" ,"cse"))
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    print(x.index("cse" ,"cse"))
TypeError: slice indices must be integers or None or have an __index__ method
>>> s1="chanti"
>>> s2="cse"
>>> s=s1+s2
>>> print(s)
chanticse
>>> s3=s1 + s2
>>> print(s3)
chanticse
>>> print(s1 + s2)
chanticse
>>> s4=s1+ " "+s2
>>> print(s4)
chanti cse
>>> y="34"
>>> print(y.isnumeric())
True
>>> y="-123"
>>> print(y.isnumeric())
False
>>> y="23.89"
>>> print(y.isnumeric())
False
>>> 