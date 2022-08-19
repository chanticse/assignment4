Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
l=[]
help(l)

print(type(l))
<class 'list'>
help(l)

l=[1,2,3,4,5,6]
print(l)
[1, 2, 3, 4, 5, 6]
l=l+[7,8,9]
print(l)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
l[0]=100
print(l)
[100, 2, 3, 4, 5, 6, 7, 8, 9]
l[-1]=200
print(l)
[100, 2, 3, 4, 5, 6, 7, 8, 200]
l.extend([11,12,13])
len(l)
12
print(l)
[100, 2, 3, 4, 5, 6, 7, 8, 200, 11, 12, 13]
l.append([2.3,4])
print(l)
[100, 2, 3, 4, 5, 6, 7, 8, 200, 11, 12, 13, [2.3, 4]]
del(1[-1])
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    del(1[-1])
TypeError: 'int' object does not support item deletion
del(l[-1])
print(l)
[100, 2, 3, 4, 5, 6, 7, 8, 200, 11, 12, 13]
l.remove[4])
SyntaxError: unmatched ')'
l.remove(4)
print(l)
[100, 2, 3, 5, 6, 7, 8, 200, 11, 12, 13]
l.pop(1)
2
l.insert(1,8888)
print(l)
[100, 8888, 3, 5, 6, 7, 8, 200, 11, 12, 13]
l.sort()
print(l)
[3, 5, 6, 7, 8, 11, 12, 13, 100, 200, 8888]
l.sort(reverse=True)
print(l)
[8888, 200, 100, 13, 12, 11, 8, 7, 6, 5, 3]
l.reverse()
print(l)
[3, 5, 6, 7, 8, 11, 12, 13, 100, 200, 8888]
l.reverse()
print(l[0])
8888
l[0]=200
print(l)
[200, 200, 100, 13, 12, 11, 8, 7, 6, 5, 3]
l2=l.copy()
print(l2)
[200, 200, 100, 13, 12, 11, 8, 7, 6, 5, 3]
l2[1]=20000
print(l2)
[200, 20000, 100, 13, 12, 11, 8, 7, 6, 5, 3]
print(l)
[200, 200, 100, 13, 12, 11, 8, 7, 6, 5, 3]
