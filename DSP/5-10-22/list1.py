Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=[1,2,3,4,5,6]
>>> prit(l)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    prit(l)
NameError: name 'prit' is not defined
>>> print(l)
[1, 2, 3, 4, 5, 6]
>>> print(l[1:4])
[2, 3, 4]
>>> print(l[-1:4])
[]
>>> print(l[4:-1])
[5]
>>> print(l[-2])
5
>>> l.reverse()
>>> print(l)
[6, 5, 4, 3, 2, 1]
>>> l=[23,4,2,21,56]
>>> print(l.sort())
None
>>> l.sort()
>>> print(l)
[2, 4, 21, 23, 56]
>>> l.sort(reverse=True)
>>> print(l)
[56, 23, 21, 4, 2]
>>> l.min()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    l.min()
AttributeError: 'list' object has no attribute 'min'
>>> print(l)
[56, 23, 21, 4, 2]
>>> print(min(l))
2
>>> print(max(l))
56
>>> l=[2,3,4,5,5,12,12]
>>> l.count(2)
1
>>> l.count(5)
2
>>> l.count(2,5)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    l.count(2,5)
TypeError: count() takes exactly one argument (2 given)
>>> l.index(4)
2
>>> l.index(5)
3
>>> l=[1,1,1]
>>> print(sum(l))
3
>>> pint("1" in l)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    pint("1" in l)
NameError: name 'pint' is not defined
>>> print("1" in l)
False
>>> print(1 in l)
True
>>> print(2 in l)
False
>>> print(clear(l))
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    print(clear(l))
NameError: name 'clear' is not defined
>>> print(l.clear())
None
>>> l.clear()
>>> print(l)
[]
>>> l2=l.copy()
>>> print(l2)
[]
>>> l=[1,1,1]
>>> l2=l.copy()
>>> print(l2)
[1, 1, 1]
>>> l.extend([2,3])
>>> print(l)
[1, 1, 1, 2, 3]
>>> print(l2)
[1, 1, 1]
>>> 