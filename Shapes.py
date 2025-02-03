import math
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, color: str):
        self.color = color

    def set_color(self, color: str):
        self.color = color

    def get_color(self) -> str:
        return self.color

    @abstractmethod
    def get_area(self) -> float:
        raise NotImplementedError("This method should be implemented by subclasses.")


class Circle(Shape):
    def __init__(self, color: str, radius: float):
        super().__init__(color)
        self.radius = radius

    def __repr__(self) -> str:
        return f"Circle (r: {self.radius}, color: {self.color})"

    def get_area(self) -> float:
        return math.pi * self.radius ** 2


class Square(Shape):
    def __init__(self, color: str, side: float):
        super().__init__(color)
        self.side = side

    def __repr__(self) -> str:
        return f"Square (a: {self.side}, color: {self.color})"

    def get_area(self) -> float:
        return self.side ** 2


class Rectangle(Shape):
    def __init__(self, color: str, length: float, width: float):
        super().__init__(color)
        self.length = length
        self.width = width

    def __repr__(self) -> str:
        return f"Rectangle (l: {self.length}, w: {self.width}, color: {self.color})"

    def get_area(self) -> float:
        return self.length * self.width


class Paint:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape: Shape) -> None:
        self.shapes.append(shape)

    def get_shapes(self) -> list:
        return self.shapes

    def calculate_total_area(self) -> float:
        total_area = sum(shape.get_area() for shape in self.shapes)
        return total_area

    def get_circles(self) -> list:
        return [shape for shape in self.shapes if isinstance(shape, Circle)]

    def get_squares(self) -> list:
        return [shape for shape in self.shapes if isinstance(shape, Square)]

    def get_rectangles(self) -> list:
        return [shape for shape in self.shapes if isinstance(shape, Rectangle)]


if __name__ == '__main__':
    paint = Paint()
    circle = Circle("blue", 10)
    square = Square("red", 11)
    rectangle = Rectangle("green", 5, 10)
    
    paint.add_shape(circle)
    paint.add_shape(square)
    paint.add_shape(rectangle)
    
    print(f"Total area: {paint.calculate_total_area()}")
    print(f"Circles: {paint.get_circles()}")
    print(f"Squares: {paint.get_squares()}")
    print(f"Rectangles: {paint.get_rectangles()}")


       
