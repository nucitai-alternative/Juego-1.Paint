"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle """
from turtle import *
from freegames import vector

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
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start, end):
    "Draw circle from start to end."
    pass  # TODO


def rectangle(start, end):
    "Draw rectangle from start to end."
    # levanta la pluma para colocarse en el punto inicial
    up()
    goto(start.x, start.y)
    # baja la pluma para comenzar a dibujar
    down()
    # comienza a rellenar el rectángulo
    begin_fill()

    # dibuja los cuatro lados utilizando el ancho y alto de los puntos
    goto(end.x, start.y)
    goto(end.x, end.y)
    goto(start.x, end.y)
    goto(start.x, start.y)

    # termina de rellenar la figura
    end_fill()


# dibuja un triángulo utilizando los puntos inicial y final
def triangle(start, end):
    "Draw triangle from start to end."
    # levanta la pluma para colocarse en el punto inicial
    up()
    goto(start.x, start.y)
    # baja la pluma para comenzar a dibujar
    down()
    # comienza a rellenar el triángulo
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
        # obtiene la figura seleccionada y utiliza el segundo clic como punto final
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        # reinicia el punto inicial para poder dibujar otra figura
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

# nuevo color agregado
# al presionar la tecla p se selecciona el color morado
onkey(lambda: color('purple'), 'P')

# mantiene abierta la ventana del programa
done()