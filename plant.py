__author__ = 'newswangerd'

import turtle

wn = turtle.Screen()

t1 = turtle.Turtle()
t1.speed(0)
t1.hideturtle()
t1.penup()
t1.goto(-500,-300)
t1.pendown()
t1.left(75)
t1.color('#86B404')

degree = 6
size = 5

angle = 25
axiom = 'X'
rules = {'X' : 'F-[[X]+X]+F[+FX]-X', 'F' : 'FF'}
for x in range(degree):
    steps = ''
    for y in axiom:
        if y in rules.keys():
            steps += rules[y]
        else:
            steps += y
    axiom = steps
print axiom
positions = []

for x in axiom:
    if x == 'F':
        t1.forward(size)
    elif x == '+':
        t1.right(angle)
    elif x == '-':
        t1.left(angle)
    elif x == '[':
        state = []
        coords = t1.pos()
        state.append(coords[0])
        state.append(coords[1])
        state.append(t1.heading())
        positions.append(state)
    elif x == ']':
        pos = positions.pop(len(positions)-1)
        t1.penup()
        t1.goto(pos[0], pos[1])
        t1.setheading(pos[2])
        t1.pendown()

wn.exitonclick()