Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

import turtle
t = turtle.Turtle()
t.shape("turtle")
>>> 
>>> color = []
>>> 
>>> color1 = input("색상 #1을 입력하시오 : ")
색상 #1을 입력하시오 : yellow
>>> color2 = input("색상 #2을 입력하시오 : ")
색상 #2을 입력하시오 : red
>>> color3 = input("색상 #3을 입력하시오 : ")
색상 #3을 입력하시오 : blue
>>> 
>>> t.fillcolor(color[1])
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    t.fillcolor(color[1])
IndexError: list index out of range
>>> t.fillcolor(color1)
>>> t.begin_fill()
>>> t.circle(50)
t.
>>> 
>>> t.end_fill()
>>> t.penup()
>>> t.goto(100,0)
>>> t.pendown()
>>> 
>>> t.fillcolor(color2)
>>> t.begin_fill()
>>> t.circle(50)
t.
>>> t.end_fill()
>>> t.penup()
>>> t.goto(200,0)
>>> t.pendown()
>>> 
>>> t.fillcolor(color3)
>>> t.begin_fill()
>>> t.circle(50)
t.
>>> t.end_fill()
