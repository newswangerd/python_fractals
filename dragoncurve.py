__author__ = 'newswangerd'

import turtle

wn = turtle.Screen()
t1 = turtle.Turtle()
t1.speed(0)
t1.hideturtle()

degree = 7
size = 2

turns = '110'
for x in range(degree):
    firstHalf = turns
    mid = turns[len(turns) / 2]
    if mid == '1':
        mid = '0'
    elif mid == '0':
        mid = '1'
    secondHalf = turns[:len(turns) / 2] + mid + turns[len(turns) / 2 + 1:]
    turns = firstHalf + '1' + secondHalf

print turns
r = 0
g = 60
b = 0
wn.colormode(255)
t1.color((r,g,b))

for (i, y) in enumerate(turns):
    t1.color((r,g,b))
    if y == '1':
        '''for t in range(3):
            t1.forward(size)
            if t != 2: t1.left(45)'''
        t1.forward(size)
        t1.left(90)
        t1.forward(size)
    elif y == '0':
        t1.forward(size)
        t1.right(90)
        t1.forward(size)
        '''for t in range(3):
            t1.forward(size)
            if t != 2: t1.right(45)'''

    r = (r + 1) % 255

    '''if r == 254:
        g = (g + 1) % 255

        if g ==  254:
            b = (b + 1) % 255'''

wn.exitonclick()