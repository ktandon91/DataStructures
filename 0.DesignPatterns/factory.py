from math import *

class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    class PointFactory:
        @staticmethod
        def new_polar_point(rho, theta):
            return Point(rho*cos(theta), rho*sin(theta))

p = Point.PointFactory.new_polar_point(1,2)