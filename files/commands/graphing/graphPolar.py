from .Graph import Graph
from sympy import *
from graphics import *
from math import *
from math import radians as rad

class GraphPolar(Graph):

    def __init__(self, size):
        Graph.__init__(self, size)

    def draw(self, expr):

        size = self.size

        temp = expr

        win = Graph.window(self)

        Graph.drawAxis(self, win)

        half = int(size / 2)

        for i in range(1000):

            expr = temp

            expr = sympify(expr)

            x = symbols('x')

            expr = expr.evalf(subs={x: i})

            point = Point(expr*cos(rad(i)) + half, half - expr*sin(rad(i)))

            point.draw(win)

        win.getMouse()
        win.close()
