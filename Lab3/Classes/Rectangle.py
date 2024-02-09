from Shapes import Shape

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length 
        self.width = width

    def area(self):
        return self.length * self.width
    

rectangle_length_width = Rectangle(2, 4)

print(rectangle_length_width.area())

