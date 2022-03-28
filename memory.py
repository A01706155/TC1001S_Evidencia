"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""


# Imports de librerias necesarias
from random import shuffle
from turtle import up, goto, down, color, begin_fill, forward,\
    left, end_fill, clear, shape, stamp, write, update,\
    ontimer, setup, addshape, hideturtle, tracer,\
    onscreenclick, done, Turtle, listen

from freegames import path


# Se define la imagen y el tamano
# del array con el que se jugara
# ademas, se ponen todos como no
# marcados y ocultos, se define el
# contador de taps y la var para
# dibujar el contador en pantalla.
car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
terminado = False
# Contador de taps
counter = {'contador': 1}
dibujador = Turtle(visible=False)


# Con este revisamos si los tiles dentro
# del rango creado en el inicio coincide
# y si no pues continuar con la ejecucion.
def check_tiles():
    for i in range(32*2):
        if hide[i]:
            return False
    return True


# Se dibujan los tiles con color negro
# a los bordes y blanco por dentro.
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


# Devuelve las coords del tile a un index.
def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


# Devuelve las coords del tile a un index.
def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


# Cuando pulsamos sobre un tile pasa lo siguiente:
def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']

    """Aqui dibujamos el contador arriba definiendo
    lo que estamos guardando, lo imprimimos y le decimos
    que queremos que sea normal y no negritas"""
    dibujador.undo()
    dibujador.write(counter['contador'], font=('Impact', 18, 'normal'))
    counter['contador'] += 1
    spot = index(x, y)

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


# Dibuja las actualizaciones y revisa cuando ya no hay tiles
def draw():
    """ Revisa si ya se acabaron los cuadros """
    if check_tiles():
        print("Se acabo el juego")

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


# Parametros de turtle
shuffle(tiles)
setup(500, 500, 370, 0)
addshape(car)
hideturtle()
tracer(False)
# Parte del contador, se va a la esquina sup izq.
dibujador.goto(-200, 200)
# Se dibuja con impact y no en negritas.
dibujador.write(counter['contador'], font=('Impact', 18, 'normal'))
clear()
listen()
onscreenclick(tap)
draw()
done()
# El dibujo ha sido completado.
terminado = True
# Imprime en consola cuando acabo y el contador.
print(terminado)
print(counter)
