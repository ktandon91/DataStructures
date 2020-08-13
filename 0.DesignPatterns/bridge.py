#used to prevent cartesian product explosion

#circle, square
#rastar( drawn in point), vector(drawn in line)

#VectorCircle, RasterCircle, VectorSq, RastarSq

# can't scale above approach

from abc import ABC

class Renderer(ABC):
    def render_circle(self, radius):
        pass

    #render sq

    #render any shape


class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print("Drawing a circle of radius {} using vector method".format(radius))

class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print("Drawing a pixels for a circle of of radius {} using rastar method".format(radius))


class Shape:
    def __init__(self, renderer):
        self.renderer = renderer

    def draw(self):pass
    def resize(self, factor): pass

class Circle(Shape):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius=radius

    def draw(self):
        self.renderer.render_circle(self.radius) ##Bridge between shape and renderer

    def resize(self, factor):
        self.radius*=factor
