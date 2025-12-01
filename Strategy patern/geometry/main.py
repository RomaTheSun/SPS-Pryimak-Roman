import math
from symtable import Class


class FigureStrategy:
    def perimeter(self):
        raise NotImplementedError()

    def area(self):
        raise NotImplementedError()

    def volume(self):
        raise NotImplementedError()


class Circle(FigureStrategy):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2

    def volume(self):
        return 0

class  RegularTriangle(FigureStrategy):
    def __init__(self, a):
        self.a = a

    def perimeter(self):
        return 3*self.a

    def area(self):
        return (math.sqrt(3) / 4) * (self.a ** 2)

    def volume(self):
        return 0

class Square(FigureStrategy):
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return 4 * self.side

    def area(self):
        return self.side ** 2

    def volume(self):
        return 0

class RegularPentagon(FigureStrategy):
    def __init__(self, a):
        self.a = a

    def perimeter(self):
        return 5 * self.a

    def area(self):
        return (1/4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * (self.a ** 2)

    def volume(self):
        return 0

class RegularHexagon(FigureStrategy):
    def __init__(self, a):
        self.a = a

    def perimeter(self):
        return 6 * self.a

    def area(self):
        return (3 * math.sqrt(3) / 2) * self.a ** 2

    def volume(self):
        return 0

class Cube(FigureStrategy):
    def __init__(self, a):
        self.a = a
    def perimeter(self):
        return 12 * self.a

    def area(self):
        return 6 * self.a ** 2

    def volume(self):
        return self.a ** 3


class Parameters:
    def __init__(self):
        self.figure_strategy = None

    def choose_figure(self, figure_name, value):
        figure_name = figure_name.lower()
        if figure_name == 'circle':
            self.figure_strategy = Circle(value)
        elif figure_name == 'square':
            self.figure_strategy = Square(value)
        elif figure_name == 'regulartriangle':
            self.figure_strategy = RegularTriangle(value)
        elif figure_name == 'regularpentagon':
            self.figure_strategy = RegularPentagon(value)
        elif figure_name == 'regularhexagon':
            self.figure_strategy = RegularHexagon(value)
        elif figure_name == 'cube':
            self.figure_strategy = Cube(value)
        else:
            raise ValueError

    def perimeter(self):
        return self.figure_strategy.perimeter()

    def area(self):
        return self.figure_strategy.area()

    def volume(self):
        return self.figure_strategy.volume()


if __name__ == '__main__':
    parameters = Parameters()
    parameters.choose_figure('cube', 3)
    print(parameters.perimeter())
    print(parameters.area())
    print(parameters.volume())
