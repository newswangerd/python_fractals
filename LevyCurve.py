__author__ = 'newswangerd'

import turtle

wn = turtle.Screen()
t1 = turtle.Turtle()
t1.speed(0)
t1.hideturtle()

degree = int(raw_input('Enter the degree: '))
size = float(raw_input('Enter the size: '))

axiom = 'F'
rules = {'F' : '+F--F+'}

for x in range(degree):
    steps = ''
    for y in axiom:
        if y in rules.keys():
            steps += rules[y]
        else:
            steps += y
    axiom = steps

for x in axiom:
    if x == 'F':
        t1.forward(size)
    elif x == '+':
        t1.left(45)
    elif x == '-':
        t1.right(45)

wn.exitonclick()