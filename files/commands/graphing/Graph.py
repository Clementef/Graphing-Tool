from sympy import *
from graphics import *

class Graph:

    size = 0

    def __init__(self, size):
        self.size = size

    def window(self):
        size = self.size
        win = GraphWin("Graph", size, size)
        return win

    def drawAxis(self, win):

        size = self.size

        half = int(size / 2)

        px1 = Point(0, half)
        px2 = Point(size, half)
        py1 = Point(half, 0)
        py2 = Point(half, size)
        c = 3
        y = 0

        xaxis = Line(px1, px2)
        yaxis = Line(py1, py2)

        xaxis.draw(win)
        yaxis.draw(win)

        for i in range(0, size, 5):
            xl = Line(Point(i, half - c), Point(i, half + 1 + c))
            xl.draw(win)

        for i in range(0, size, 5):
            yl = Line(Point(half - c, i), Point(half + 1 + c, i))
            yl.draw(win)

