"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""
from random import shuffle
from turtle import up, goto, down, color, begin_fill, forward,\
    left, end_fill, clear, shape, stamp, write, update,\
    ontimer, setup, addshape, hideturtle, tracer,\
    onscreenclick, done, Turtle, listen

from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
terminado = False
# Contador de taps
counter = {'contador': 0}
dibujador = Turtle(visible=False)


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']

    dibujador.undo()
    dibujador.write(counter['contador'], font=('Impact', 18, 'normal'))
    counter['contador'] += 1
    clear()
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def draw():
    """ Revisa si ya se acabaron los cuadros """
    if check_tiles():
        dibujador.undo()
        clear()
        dibujador.write("Se acabo", font=('Impact', 30, 'normal'))

    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()
    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 20, 'normal'))

    update()
    ontimer(draw, 100)


def check_tiles():
    for i in range(64):
        if hide[i]:
            return False
    return True


shuffle(tiles)
setup(500, 500, 370, 0)
addshape(car)
hideturtle()
tracer(False)
dibujador.goto(-200, 200)
dibujador.color('black')
dibujador.write(counter['contador'], font=('Impact', 18, 'normal'))
clear()
listen()
onscreenclick(tap)
draw()
done()
# El dibujo ha sido completado
terminado = True
print(terminado)
print(counter)
