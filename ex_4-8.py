Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> import turtle
>>> t = turtle.Turtle()
>>> t.shape("turtle")
>>> 
>>> x1 = int(input("x1 : "))
x1 : 0
>>> y1 = int(input("y1 : "))
y1 : 0
>>> x2 = int(input("x2 : "))
x2 : 100
>>> y2 = int(input("y2 : "))
y2 : 100
>>> x3 = int(input("x3 : "))
x3 : 200
>>> y3 = int(input("y3 = "))
y3 = 100
>>> 
>>> a = [x1,y1]
>>> b = [x2,y2]
>>> c = [x3,y3]
>>> 
>>> t.goto(a)
>>> t.goto(b)
>>> t.goto(c)
