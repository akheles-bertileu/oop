from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height




x = "global x"


def outer_function():
    x = "enclosing x"

    def inner_function():
        x = "local x"
        print("Inside inner_function:", x)

    inner_function()
    print("Inside outer_function:", x)




def func_a():
    print("Function A is called")
    from types import SimpleNamespace
    ns = SimpleNamespace()

    def func_b():
        print("Function B is called")
        print("Function B does not call A to avoid circular import")

    ns.func_b = func_b
    ns.func_b()

