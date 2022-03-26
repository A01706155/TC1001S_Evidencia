"""Pacman, classic arcade game.

Exercises:

1. Change the board.
2. Make the ghosts faster.
"""
# Importación de librerías random
from random import choice
from turtle import bgcolor, clear, done, up, goto, dot, update, ontimer,\
    setup, hideturtle, tracer, listen, onkey, Turtle

from freegames import floor, vector

# Inicializa las variables del puntaje
# y el entorno grafico de Turtle:
state = {'score': 0}
path = Turtle(visible=False)
writer = Turtle(visible=False)
aim = vector(5, 0)
# Define las ubicaciones de inicio de
pacman = vector(-20, -180)
ghosts = [
    [vector(-160, 160), vector(15, 0)],
    [vector(-160, 0), vector(0, 15)],
    [vector(120, 160), vector(0, -15)],
    [vector(120, 0), vector(-15, 0)],
]
# fmt: off
# A través de este array se define el tablero del juego:
tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0,
    0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0,
    0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0,
    0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0,
    0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0,
    0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0,
    0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0,
    0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0,
    0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]
# fmt: on

# Funcion de square, dibuja el tablero usando
# el camino definido entre (x, y)


def square(x, y):

    """Draw square using path at (x, y)."""
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for count in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()

# Funcion offset, compensa la posicion de cada punto
# de cada tile utilizando 20 pixeles de distancia.


def offset(point):
    """Return offset of point in tiles."""
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index

# Funcion valid, valida la posicion a donde se de-
# be de mover algo es accesible o no hay colision.


def valid(point):
    """Return True if point is valid in tiles."""
    index = offset(point)

    if tiles[index] == 0:
        return False

    index = offset(point + 19)

    if tiles[index] == 0:
        return False

    return point.x % 20 == 0 or point.y % 20 == 0

# Funcion mundo, dibuja el mundo de acuerdo al camino
# realizado y luego lo muestra en pantalla con Turtle


def world():
    """Draw world using path."""
    bgcolor('black')
    path.color('blue')

    for index in range(len(tiles)):
        tile = tiles[index]

        if tile > 0:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)

            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(2, 'white')

# Funcion mover, sirve para mover a pacman y a los
# fantasmas, también actualiza el puntaje en pantalla.


def move():
    """Move pacman and all ghosts."""
    writer.undo()  # Borra el puntaje
    writer.write(state['score'])  # Escribe el puntaje

    clear()  # Limpia la pantalla

    # Valida si pacman no colisiona, permite
    # el cambio de direccion por cada ciclo
    if valid(pacman + aim):
        pacman.move(aim)

    index = offset(pacman)

    # Por cada punto tocado, sube el score
    if tiles[index] == 1:
        tiles[index] = 2
        state['score'] += 1
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)

    # A continuacion se define la posicion
    # dibujada de pac-man en pantalla.
    up()
    goto(pacman.x + 10, pacman.y + 10)
    dot(20, 'yellow')

    # En esta parte se define parte de la "inteligencia"
    # de los fantamas y su velocidad de movimiento.
    for point, course in ghosts:
        if valid(point + course):
            point.move(course)
        else:
            options = [
                vector(15, 0),
                vector(-15, 0),
                vector(0, 15),
                vector(0, -15),
            ]
            plan = choice(options)
            course.x = plan.x
            course.y = plan.y

        up()
        goto(point.x + 10, point.y + 10)
        dot(20, 'red')

    # Actualiza la pantalla
    update()

    for point, course in ghosts:
        if abs(pacman - point) < 20:
            return

    # Por cada 100ms todo se mueve
    ontimer(move, 100)

# Revisa la direccion de pacman y la
# valida cada vez que se solicita.


def change(x, y):
    """Change pacman aim if valid."""
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y

# Define parametros de Turtle


setup(420, 420, 370, 0)
hideturtle()
tracer(False)

# Define posicion, color y valor
# del puntaje en pantalla.


writer.goto(160, 160)
writer.color('white')
writer.write(state['score'])
listen()

# Velocidad y direccion de pacman


onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
onkey(lambda: change(-5, 0), 'Left')

# Parametros de actualizacion


world()
move()
done()
