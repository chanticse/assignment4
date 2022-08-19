Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #upper()
>>> a="bfyf"
>>> print(a.upper())
BFYF
>>> b="rgukt123"
>>> print(b.upper())
RGUKT123
>>> str="python is good"
>>> print(str.capitalize())
Python is good
>>> str="123rgukt"
>>> print(str.capitalize())
123rgukt
>>> str="123 rgukt "
>>> print(str.capitalize())
123 rgukt 
>>> str="rgukt123"
>>> print(str.capitalize())
Rgukt123
>>> str="rgukt 123"
>>> print(str.capitalize())
Rgukt 123
>>> #casefold: converts into lower case
>>> str="naTUre iS So BEAUtiful"
>>> print(str.casefold())
nature is so beautiful
>>> #center():returns a centerd string
>>> str="chanti"
>>> print(str.center(50))
                      chanti                      
>>> print(str.(center(30,cse))
      
SyntaxError: invalid syntax
>>> print(str.center(30,"cse"))
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print(str.center(30,"cse"))
TypeError: The fill character must be exactly one character long
>>> print(str.center(30,"a"))
aaaaaaaaaaaachantiaaaaaaaaaaaa
>>> #count():returns count of a specified value
>>> str="chanti cse chanti cse"
>>> print(str.count("chanti"))
2
>>> print(str.counnt("c"))
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print(str.counnt("c"))
AttributeError: 'str' object has no attribute 'counnt'
>>> print(str.count("c"))
4
>>> print(str.count("e"))
2
>>> print(str.count("chanti" "cse"))
0
>>> print(str.count("chanti","cse"))
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    print(str.count("chanti","cse"))
TypeError: slice indices must be integers or None or have an __index__ method
>>> print(str.count("nature"))
0
>>> 