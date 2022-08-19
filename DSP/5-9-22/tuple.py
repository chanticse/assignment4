Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> t=(1,2,3)
>>> type(t)
<class 'tuple'>
>>> print(t)
(1, 2, 3)
>>> t[0]=10
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    t[0]=10
TypeError: 'tuple' object does not support item assignment
>>> x=list(t)
>>> type(t)
<class 'tuple'>
>>> type(x)
<class 'list'>
>>> x[0]=888
>>> print(x)
[888, 2, 3]
>>> print(t)
(1, 2, 3)
>>> t=tuple(x)
>>> print(t)
(888, 2, 3)
>>> #sets
>>> s1={1,2,3}
>>> print(s1)
{1, 2, 3}
>>> s2={3,4,5}
>>> print(s2)
{3, 4, 5}
>>> type(s1)
<class 'set'>
>>> print(s1)
{1, 2, 3}
>>> print(s2)
{3, 4, 5}
>>> s1.union(s2)
{1, 2, 3, 4, 5}
>>> s1.intersection(s2)
{3}
>>> s1.difference(s2)
{1, 2}
>>> s2.difference(s1)
{4, 5}
>>> print(s1)
{1, 2, 3}
>>> s1.update({6,7,8})
>>> print(s1)
{1, 2, 3, 6, 7, 8}
>>> #set is unordered list
>>> s1.difference_update(s2)
>>> print(s1)
{1, 2, 6, 7, 8}
>>> print(s1)
{1, 2, 6, 7, 8}
>>> s1.add({22,44})
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    s1.add({22,44})
TypeError: unhashable type: 'set'
>>> s1.add(22)
>>> print(s1)
{1, 2, 6, 7, 8, 22}
>>> s1.pop()
1
>>> print(s1)
{2, 6, 7, 8, 22}
>>> s1.clear()
>>> print(s1)
set()
>>> s1={1,2,3,4}
>>> print(s1)
{1, 2, 3, 4}
>>> s1.pop()
1
>>> s1.pop()
2
>>> print(s1)
{3, 4}
>>> print(s1)
{3, 4}
>>> s=s1.copy()
>>> print(s)
{3, 4}
>>> s2=s.copy()
>>> print(s2)
{3, 4}
>>> print(s1,s2)
{3, 4} {3, 4}
>>> s.add(22324)
>>> print(s)
{3, 4, 22324}
>>> s.remove(4)
>>> print(s)
{3, 22324}
>>> s1={1,2,3}
>>> s2={4,5,6}
>>> print(s1)
{1, 2, 3}
>>> print(s2)
{4, 5, 6}
>>> s3={4,2,5}
>>> print(s3)
{2, 4, 5}
>>> s1.symmetric_difference(s2)
{1, 2, 3, 4, 5, 6}
>>> s1.symmetric_difference(s3)
{1, 3, 4, 5}
>>> s4={}
>>> print(s4)
{}
>>> print(s1)
{1, 2, 3}
>>> print(s1.symmetric_difference(s4))
{1, 2, 3}
>>> s={1,2,3,45,6}
>>> s1={1,2,3}
>>> print(s.issubset(s1))
False
>>> print(s1.subset(s))
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    print(s1.subset(s))
AttributeError: 'set' object has no attribute 'subset'
>>> print(s1.issubset(s))
True
>>> print(s.issuperset(s1))
True
>>> print(s)
{1, 2, 3, 6, 45}
>>> print(s2)
{4, 5, 6}
>>> s.update({22,33})
>>> print(s)
{1, 2, 3, 33, 6, 45, 22}
>>> print(s.symmetric_difference(s2))
{1, 2, 3, 4, 5, 33, 45, 22}
>>> print(s.symmetric_difference_update(s2))
None
>>> s.symmetric_difference_update(s2))
SyntaxError: unmatched ')'
>>> s.symmetric_difference_update(s2)
>>> print(s)
{1, 2, 3, 33, 6, 45, 22}
>>> x={1,2,3,4}
>>> y={5,6,7,8}
>>> x.isdisjoint(y)
True
>>> z={3,5}
>>> x.isdisjoint(z)
False
>>> print(s)
{1, 2, 3, 33, 6, 45, 22}
>>> s.discard(6)
>>> print(s)
{1, 2, 3, 33, 45, 22}
>>> 