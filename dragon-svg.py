__author__ = 'newswangerd'
import svgwrite


def main():
    degree = 10
    size = 2

    turns = dragon_code(degree)
    state = 0
    coords = (0,0)

    img = svgwrite.Drawing('test.svg', profile='tiny')
    total = len(turns)

    for (i, y) in enumerate(turns):
        if y == '1':
           coords =  draw(state, coords, img, size, i, total)
           state = (state + 1) % 4
           coords =  draw(state, coords, img, size, i, total)
           #state = (state + 1) % 4
        elif y == '0':
           coords =  draw(state, coords, img, size, i, total)
           state = (state - 1) % 4
           coords =  draw(state, coords, img, size, i, total)
           #state = (state - 1) % 4
    img.save()

def draw(state, coords, img, size, current, total):
    if state == 0:
        new_coords = (coords[0] + size, coords[1])
    elif state == 1:
        new_coords = (coords[0], coords[1] - size)
    elif state == 2:
        new_coords = (coords[0] - size, coords[1])
    elif state == 3:
        new_coords = (coords[0], coords[1] + size)


    img.add(img.line(coords, new_coords, stroke=svgwrite.rgb(0, 0,float(current)/float(total) * 100, '%')))

    return new_coords

def dragon_code(degree):
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
    return turns

main()