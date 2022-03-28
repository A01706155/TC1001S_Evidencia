"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
"""

# Importa librerias turtle y freegames
from turtle import up, goto, down, circle, update, setup, hideturtle,\
    tracer, onscreenclick, done, color

from freegames import line


# Campo de juego
def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


# Dibuja la X
def drawx(x, y):
    """Draw X player."""
    line(x+33.5, y+25, x + 100, y + 100)
    line(x+33.5, y + 100, x + 100, y+25)
    color('red')


# Dibuja el circulo
def drawo(x, y):
    """Draw O player."""
    up()
    goto(x + 67, y + 50)
    down()
    circle(22)
    color('blue')


# Redondea un valor para ajustar a la cuadricula
def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


# Especifica que juegador esta jugando
state = {'player': 0}
# Da el arreglo de ambos jugadores
players = [drawx, drawo]
# Define un arreglo de posibles ocupantes
ocupados = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


# Dibuja X/O y revisa si el espacio esta ocupado
def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    player = state['player']
    draw = players[player]
    if x == -200 and y == 66:
        if ocupados[0] == " ":
            ocupados[0] = 1
            draw(x, y)
            update()
            state['player'] = not player
        elif ocupados[0] != "":
            print("No disponible")

    elif x == -200 and y == -200:
        if ocupados[6] == " ":
            ocupados[6] = 1
            draw(x, y)
            update()
        elif ocupados[6] != "":
            print("No disponible")

    elif x == 66 and y == -200:
        if ocupados[8] == " ":
            ocupados[8] = 1
            draw(x, y)
            update()
        elif ocupados[8] != "":
            print("No disponible")

    elif x == 66 and y == -67:
        if ocupados[5] == " ":
            ocupados[5] = 1
            draw(x, y)
            update()
        elif ocupados[5] != "":
            print("No disponible")

    elif x == -67 and y == -200:
        if ocupados[7] == " ":
            ocupados[7] = 1
            draw(x, y)
            update()
        elif ocupados[7] != "":
            print("No disponible")

    elif x == -200 and y == -67:
        if ocupados[3] == " ":
            ocupados[3] = 1
            draw(x, y)
            update()
        elif ocupados[3] != "":
            print("No disponible")

    elif x == -67 and y == -67:
        if ocupados[4] == " ":
            ocupados[4] = 1
            draw(x, y)
            update()
        elif ocupados[4] != "":
            print("No disponible")

    elif x == -67 and y == 66:
        if ocupados[1] == " ":
            ocupados[1] = 1
            draw(x, y)
            update()
            state['player'] = not player
        elif ocupados[1] != "":
            print("No disponible")

    elif x == 66 and y == 66:
        if ocupados[2] == " ":
            ocupados[2] = 1
            draw(x, y)
            update()
        elif ocupados[2] != "":
            print("No disponible")

    state['player'] = not player


# Parametros de turtle
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
