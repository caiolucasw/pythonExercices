'''Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.

'''

from math import pi

class Circle:

    def __init__(self, radius):
        self.radius = radius
        self.area = self.calculaArea()

    def calculaArea(self):
        return pi*(self.radius**2)


# Exercicio 48 - Define a class named Rectangle which can be constructed by a length and width.
# The Rectangle class has a method which can compute the area.

class Rectangle():

    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.area = self.calculaArea()

    def calculaArea(self):
        return self.length*self.width


#Exercicio 49 - Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument.
# Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

class Shape():

    def calculaArea(self):
        return 0


class Square(Shape):

    def __init__(self, length):
        self.length = length

    def calculaArea(self):
        return self.length**2



circulo = Circle(5)
print(circulo.area)
retangulo = Rectangle(5,4)
print(retangulo.area)


