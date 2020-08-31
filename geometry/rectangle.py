# pytest-tutorial/geometry/rectangle.py


class Rectangle:
    def __init__(self, length: int, width: int) -> None:
        self.length = length
        self.width = width

    def area(self) -> int:
        if not isinstance(self.length, int) or not isinstance(self.width, int):
            raise TypeError("Rectangle length and width should be of type int")
        area = self.length * self.width
        if area < 0:
            raise ValueError("Area of a geometry can't be smaller than 0")
        return area

    def perimeter(self):
        return 2 * self.length + 2 * self.width
