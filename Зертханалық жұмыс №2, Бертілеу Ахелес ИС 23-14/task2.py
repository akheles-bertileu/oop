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

def main():
    circle = Circle(5)
    rectangle = Rectangle(4, 6)

    print(f"Circle area: {circle.area()}")
    print(f"Rectangle area: {rectangle.area()}")

if __name__ == "__main__":
    main()
