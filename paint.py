"""
Paint utilizando Turtle Graphics.

Funcionalidades:
- Dibujar líneas.
- Dibujar cuadrados.
- Dibujar círculos.
- Dibujar rectángulos.
- Dibujar triángulos.
- Cambiar entre varios colores.
- Deshacer el último dibujo con la tecla U.

Autores:
[Nombre de los integrantes]

Fecha:
[Fecha de entrega]
"""

from turtle import *
from freegames import vector
import math


def line(start, end):
    """
    Dibuja una línea entre dos puntos.

    Parámetros:
        start (vector): Punto inicial.
        end (vector): Punto final.
    """
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """
    Dibuja un cuadrado utilizando la distancia horizontal
    entre los puntos inicial y final.
    """
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start, end):
    """
    Dibuja un círculo tomando como radio la distancia
    entre el punto inicial y el punto final.
    """
    up()
    goto(start.x, start.y)

    # Calcula el radio mediante la fórmula de distancia
    radius = math.sqrt(
        (end.x - start.x) ** 2 +
        (end.y - start.y) ** 2
    )

    down()
    begin_fill()
    turtle.circle(radius)
    end_fill()


def rectangle(start, end):
    """
    Dibuja un rectángulo utilizando los puntos inicial
    y final para determinar ancho y alto.
    """
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    goto(end.x, start.y)
    goto(end.x, end.y)
    goto(start.x, end.y)
    goto(start.x, start.y)

    end_fill()


def triangle(start, end):
    """
    Dibuja un triángulo isósceles utilizando los puntos
    inicial y final.
    """
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    # Base del triángulo
    goto(end.x, start.y)

    # Vértice superior
    goto((start.x + end.x) / 2, end.y)

    # Regresa al punto inicial
    goto(start.x, start.y)

    end_fill()


def tap(x, y):
    """
    Guarda el primer clic como punto inicial.
    Cuando se realiza un segundo clic, dibuja
    la figura seleccionada.
    """
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)

    else:
        shape = state['shape']
        end = vector(x, y)

        shape(start, end)

        state['start'] = None


def store(key, value):
    """
    Guarda una configuración en el estado del programa.

    Parámetros:
        key: Nombre de la propiedad.
        value: Valor que se desea almacenar.
    """
    state[key] = value


# Estado del programa
state = {
    'start': None,
    'shape': line
}

# Configuración de la ventana
setup(420, 420, 370, 0)

# Detecta clics del usuario
onscreenclick(tap)

# Activa la escucha del teclado
listen()

# Permite deshacer el último dibujo
onkey(undo, 'u')

# Colores disponibles
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')

# Nuevo color agregado
onkey(lambda: color('purple'), 'P')

# Selección de figuras
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')

# Mantiene abierta la aplicación
done()
