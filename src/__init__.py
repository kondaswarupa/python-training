from math import pi
class Shape:
   def __init__(self, name):
        self.name = name
   def area(self):
        pass
   def fact(self):
        return "I am a two-dimensional shape."
   def __str__(self):
        return self.name


class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length

    def area(self):
        return self.length**2

    def fact(self):
        return "Squares have each angle equal to 90 degrees."
