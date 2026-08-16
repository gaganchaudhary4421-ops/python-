class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * (self.radius ** 2)

    def Perimeter(self):
        return 2 * 3.14159 * self.radius
Area=circle(5).area()
perimeter=circle(5).Perimeter()
print("Area of the circle:", Area)
print("Perimeter of the circle:", perimeter)