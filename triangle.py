__author__ = 'newswangerd'

import turtle
import time

wn = turtle.Screen()

t1 = turtle.Turtle()
t1.speed(0)
t1.hideturtle()
t1.penup()
t1.goto(-100,150)
t1.pendown()

degree = 6
size = 6

angle = 120
axiom = 'F-G-G'
rules = {'F' : 'F-G+F+G-F', 'G' : 'GG'}

for x in range(degree):
    steps = ''
    for y in axiom:
        if y in rules.keys():
            steps += rules[y]
        else:
            steps += y
    axiom = steps

for y in range(2):
    for x in axiom:
        if x == 'F' or x == 'G':
            t1.forward(size)
        elif x == '+':
            t1.left(angle)
        elif x == '-':
            t1.right(angle)
    t1.right(angle)
    time.sleep(3)
    t1.color('white')

wn.exitonclick()