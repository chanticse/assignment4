Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=[1,2,3,4]
>>> print(l)
[1, 2, 3, 4]
>>> l=l+[5,6,7,8]
>>> print(l)
[1, 2, 3, 4, 5, 6, 7, 8]
>>> l.insert(o,10)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    l.insert(o,10)
NameError: name 'o' is not defined
>>> l.insert(0,10)
>>> print(l)
[10, 1, 2, 3, 4, 5, 6, 7, 8]
>>> l.insert(2,9)
>>> print(l)
[10, 1, 9, 2, 3, 4, 5, 6, 7, 8]
>>> l.append([2.3,4])
>>> print(l)
[10, 1, 9, 2, 3, 4, 5, 6, 7, 8, [2.3, 4]]
>>> print(l[10])
[2.3, 4]
>>> print(l[-1])
[2.3, 4]
>>> print(l[:10])
[10, 1, 9, 2, 3, 4, 5, 6, 7, 8]
>>> print(l[:11])
[10, 1, 9, 2, 3, 4, 5, 6, 7, 8, [2.3, 4]]
>>> print(l[-1:5])
[]
>>> print([5:-1])
SyntaxError: invalid syntax
>>> print(l[5:-1])
[4, 5, 6, 7, 8]
>>> l.extend(23,22)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    l.extend(23,22)
TypeError: extend() takes exactly one argument (2 given)
>>> l.extend([22,34])
>>> print(l)
[10, 1, 9, 2, 3, 4, 5, 6, 7, 8, [2.3, 4], 22, 34]
>>> print(len(l))
13
>>> del([0])
SyntaxError: cannot delete literal
>>> del(l[0])
>>> print(l)
[1, 9, 2, 3, 4, 5, 6, 7, 8, [2.3, 4], 22, 34]
>>> del(l[-1])
>>> print(l)
[1, 9, 2, 3, 4, 5, 6, 7, 8, [2.3, 4], 22]
>>> print(len(l))
11
>>> l.remove(9)
>>> print(l)
[1, 2, 3, 4, 5, 6, 7, 8, [2.3, 4], 22]
>>> print(l)
[1, 2, 3, 4, 5, 6, 7, 8, [2.3, 4], 22]
>>> l.pop()
22
>>> print(l)
[1, 2, 3, 4, 5, 6, 7, 8, [2.3, 4]]
>>> l.pop(3)
4
>>> print(l)
[1, 2, 3, 5, 6, 7, 8, [2.3, 4]]
>>> 