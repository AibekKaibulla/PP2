import math

class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)
    
    def move(self, x1, y1):
        self.x += x1
        self.y += y1

    def dist(self, new_point):
        x1 = new_point.x - self.x
        y1 = new_point.y - self.y
        distance = math.sqrt(x1**2 + y1**2)
        return distance


point1 = Point(2, 3)
point2 = Point(5, 6)

point1.show()
point2.show()

print("distance: ", point1.dist(point2))

point1.move(2, 3)
point1.show()