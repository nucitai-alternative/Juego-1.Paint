
"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle
"""

from turtle import *
from freegames import vector
from math import hypot


# dibuja una línea entre dos puntos
def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


# dibuja un cuadrado utilizando el punto inicial y final
def square(start, end):
    "Draw square from start to end."
    # calcula el tamaño del cuadrado dependiendo del movimiento del mouse
    side = max(abs(end.x - start.x), abs(end.y - start.y))

    # identifica hacia qué dirección se va a dibujar
    x = side if end.x >= start.x else -side
    y = side if end.y >= start.y else -side

    # se coloca en el punto inicial
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    # dibuja los cuatro lados del cuadrado
    goto(start.x + x, start.y)
    goto(start.x + x, start.y + y)
    goto(start.x, start.y + y)
    goto(start.x, start.y)

    end_fill()


# dibuja un círculo utilizando el punto inicial como centro
def circle(start, end):
    "Draw circle from start to end."
    # calcula el radio usando la distancia entre los dos puntos
    radius = hypot(end.x - start.x, end.y - start.y)

    # se coloca en la parte inferior del círculo
    up()
    goto(start.x, start.y - radius)
    setheading(0)
    down()
    begin_fill()

    # dibuja el círculo con el radio calculado
    circle(radius)

    end_fill()


# dibuja un rectángulo utilizando los puntos inicial y final
def rectangle(start, end):
    "Draw rectangle from start to end."
    # se coloca en el punto inicial
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    # dibuja los cuatro lados del rectángulo
    goto(end.x, start.y)
    goto(end.x, end.y)
    goto(start.x, end.y)
    goto(start.x, start.y)

    # termina de rellenar la figura
    end_fill()


# dibuja un triángulo utilizando los puntos inicial y final
def triangle(start, end):
    "Draw triangle from start to end."
    # se coloca en el punto inicial
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    # dibuja los tres lados del triángulo
    goto(end.x, start.y)
    goto((start.x + end.x) / 2, end.y)
    goto(start.x, start.y)

    # termina de rellenar la figura
    end_fill()


# guarda el punto inicial o dibuja la figura seleccionada
def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        # guarda la primera posición donde se hizo clic
        state['start'] = vector(x, y)
    else:
        # obtiene la figura seleccionada y el segundo punto
        shape = state['shape']
        end = vector(x, y)

        # dibuja la figura con los dos puntos
        shape(start, end)

        # reinicia el punto inicial para dibujar otra figura
        state['start'] = None


# guarda la opción seleccionada en el estado del programa
def store(key, value):
    state[key] = value


# establece el estado inicial y la figura seleccionada
state = {'start': None, 'shape': line}

# configura el tamaño y la posición de la ventana
setup(420, 420, 370, 0)

# permite dibujar haciendo clic en la pantalla
onscreenclick(tap)
listen()

# permite deshacer el último dibujo con la tecla u
onkey(undo, 'u')

# selecciona los colores disponibles mediante el teclado
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')

# permite seleccionar la figura que se quiere dibujar
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')

# agrega el color morado al programa
# al presionar la tecla p se selecciona este color
onkey(lambda: color('purple'), 'P')

# mantiene abierta la ventana del programa
done()
