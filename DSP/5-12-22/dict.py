Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> d={}
>>> type(d)
<class 'dict'>
>>> d["name"]="chanti"
>>> print(d)
{'name': 'chanti'}
>>> d["rno"]=1
>>> print(d)
{'name': 'chanti', 'rno': 1}
>>> len(d)
2
>>> d["rno"]=7
>>> print(d)
{'name': 'chanti', 'rno': 7}
>>> d["b"]="cse"
>>> print(d)
{'name': 'chanti', 'rno': 7, 'b': 'cse'}
>>> del(["name"])
SyntaxError: cannot delete literal
>>> del(d["name"])
>>> print(d)
{'rno': 7, 'b': 'cse'}
>>> d.popitm()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    d.popitm()
AttributeError: 'dict' object has no attribute 'popitm'
>>> d.popitem()
('b', 'cse')
>>> print(d)
{'rno': 7}
>>> d.pop("rno")
7
>>> print(d)
{}
>>> d=dict9([(1,2),(3,4),(5,7)])
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    d=dict9([(1,2),(3,4),(5,7)])
NameError: name 'dict9' is not defined
>>> d=dict([(1,2),(3,4),(5,7)])
>>> print(d)
{1: 2, 3: 4, 5: 7}
>>> d.keys()
dict_keys([1, 3, 5])
>>> d.values()
dict_values([2, 4, 7])
>>> d.items()
dict_items([(1, 2), (3, 4), (5, 7)])
>>> d.get(1)
2
>>> d.get(5)
7
>>> d.get(4)
>>> print(d)
{1: 2, 3: 4, 5: 7}
>>> d=dict([(2,4),(name,chanti),(rno,9)])
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    d=dict([(2,4),(name,chanti),(rno,9)])
NameError: name 'name' is not defined
>>> d=dict([(2,4),("name","chanti"),("rno",9)])
>>> print(d)
{2: 4, 'name': 'chanti', 'rno': 9}
>>> len(d)
3
>>> d.keys()
dict_keys([2, 'name', 'rno'])
>>> d.values()
dict_values([4, 'chanti', 9])
>>> d.items()
dict_items([(2, 4), ('name', 'chanti'), ('rno', 9)])
>>> help(d)
Help on dict object:

class dict(object)
 |  dict() -> new empty dictionary
 |  dict(mapping) -> new dictionary initialized from a mapping object's
 |      (key, value) pairs
 |  dict(iterable) -> new dictionary initialized as if via:
 |      d = {}
 |      for k, v in iterable:
 |          d[k] = v
 |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
 |      in the keyword argument list.  For example:  dict(one=1, two=2)
 |  
 |  Methods defined here:
 |  
 |  __contains__(self, key, /)
 |      True if the dictionary has the specified key, else False.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(self, /)
 |      Return a reverse iterator over the dict keys.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(...)
 |      D.__sizeof__() -> size of D in memory, in bytes
 |  
 |  clear(...)
 |      D.clear() -> None.  Remove all items from D.
 |  
 |  copy(...)
 |      D.copy() -> a shallow copy of D
 |  
 |  get(self, key, default=None, /)
 |      Return the value for key if key is in the dictionary, else default.
 |  
 |  items(...)
 |      D.items() -> a set-like object providing a view on D's items
 |  
 |  keys(...)
 |      D.keys() -> a set-like object providing a view on D's keys
 |  
 |  pop(...)
 |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
 |      If key is not found, d is returned if given, otherwise KeyError is raised
 |  
 |  popitem(self, /)
 |      Remove and return a (key, value) pair as a 2-tuple.
 |      
 |      Pairs are returned in LIFO (last-in, first-out) order.
 |      Raises KeyError if the dict is empty.
 |  
 |  setdefault(self, key, default=None, /)
 |      Insert key with a value of default if key is not in the dictionary.
 |      
 |      Return the value for key if key is in the dictionary, else default.
 |  
 |  update(...)
 |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
 |      If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
 |      If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
 |      In either case, this is followed by: for k in F:  D[k] = F[k]
 |  
 |  values(...)
 |      D.values() -> an object providing a view on D's values
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  fromkeys(iterable, value=None, /) from builtins.type
 |      Create a new dictionary with keys from iterable and values set to value.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> d=dict([(2,4),(name,chanti),(rno,9)])
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    d=dict([(2,4),(name,chanti),(rno,9)])
NameError: name 'name' is not defined
>>> d=dict([(2,4),("name","chanti"),("rno",9)])
>>> print(d)
{2: 4, 'name': 'chanti', 'rno': 9}
>>> d.clear()
>>> print(d)
{}
>>> d=dict([(2,4),("name","chanti"),("rno",9)])
>>> print(d)
{2: 4, 'name': 'chanti', 'rno': 9}
>>> d1=d.copy()
>>> print(d1)
{2: 4, 'name': 'chanti', 'rno': 9}
>>> 