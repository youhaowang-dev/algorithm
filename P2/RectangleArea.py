# https://www.lintcode.com/problem/454/
# Implement a Rectangle class which include the following attributes and methods:

# Two public attributes width and height.
# A constructor which expects two parameters width and height of type int.
# A method getArea which would calculate the size of the rectangle and return.


class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def getArea(self) -> int:
        return self.width * self.height
