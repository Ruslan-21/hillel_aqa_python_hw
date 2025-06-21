from abc import ABC, abstractmethod
import math
class Figure(ABC):
    @abstractmethod

    def area(self):
        pass

    @abstractmethod

    def perimeter(self):
        pass

class Rectangle(Figure):

    def __init__(self, height, weight):
        self.height = height
        self.weight = weight


    def area(self):
         return self.height * self.weight
    def perimeter(self):
         return (self.height + self.weight) * 2


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c, height):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.height = height



    def area(self):
        return 0.5 * self.side_a * self.height
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c



class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return math.pi * 2 * self.radius


figures = [
    Rectangle(4, 6),
    Triangle(3, 4, 5, 2.4),
    Circle(5)
]

for figure in figures:
    if isinstance(figure, Rectangle):
        print("Прямокутник:")
    elif isinstance(figure, Triangle):
        print("Трикутник:")
    elif isinstance(figure, Circle):
        print("Коло:")
    else:
        print("Фігура:")

    print(f"Площа: {figure.area()}")
    print(f"Периметр: {figure.perimeter()}")




