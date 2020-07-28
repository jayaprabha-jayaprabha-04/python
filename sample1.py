Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:/Users/Jayaprabha Shree/AppData/Local/Programs/Python/Python38-32/sampl1.py
>>> a=10
>>> type(a)
<class 'int'>
>>> print(a)
10
>>> b=20
>>> type(b)
<class 'int'>
>>> print(b)
20
>>> c=a+b
>>> print(c)
30
>>> type(c)
<class 'int'>
>>> d=12.5
>>> type(d)
<class 'float'>
>>> e=c+d
>>> print(e)
42.5
>>> f=4+5j
>>> type(f)
<class 'complex'>
>>> g=e+f
>>> print(g)
(46.5+5j)
>>> type(g)
<class 'complex'>
>>> a
10
>>> b
20
>>> c
30
>>> d
12.5
>>> e
42.5
>>> f
(4+5j)
>>> g
(46.5+5j)
>>> x="enter the value1"
>>> x
'enter the value1'
>>> y=enter the value 2
SyntaxError: invalid syntax
>>> y="enter the value 2"
>>> y
'enter the value 2'
>>> type(x)
<class 'str'>
>>> a1=a-b
>>> a1
-10
>>> b1=b*c
>>> b1
600
>>> type(a1)
<class 'int'>
>>> c1=d**e
>>> 
>>> c1
4.15600013356459e+46
>>> d1=2/2
>>> d1
1.0
>>> d2=2//2
>>> d2
1
>>> e1=f%a
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    e1=f%a
TypeError: can't mod complex numbers.
>>> e1=c%e
>>> e1
30.0
>>> a1=a**b
>>> a1
100000000000000000000
>>> x1=5e4
>>> x1
50000.0
>>> 