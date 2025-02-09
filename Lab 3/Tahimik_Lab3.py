# LAB 3 - Tahimik, Allysa

# Create the classes
class Shape():
    def __init__(self):
        pass

# Calculate the rectangle area
class Rectangle(Shape):
    def __init__(self, l, w):
        self.length = l
        self.width = w
    def getArea(self):
        return self.length * self.width

# Calculate the circle area
class Circle(Shape):
    def __init__(self, r):
        self.radius = r
    def getArea(self):
        return 3.14 * self.radius * self.radius

# Calculate the triangle area
class Triangle(Shape):
    def __init__(self, b, h):
        self.base = b
        self.height = h
    def getArea(self):
        return 0.5 * self.base * self.height


# Read txt file
file = open(r'D:\actual homework\TAMU GIST\GEO676 - GIS PROGRAMMING\Module 3 - Object Oriented Programming\shape.txt', 'r')
lines = file.readlines()
file.close()

# Read file and print results
for line in lines:
    components = line.split(',')
    shape = components[0]

    if shape == 'Rectangle':
        rect = Rectangle(int(components[1]), int(components[2]))
        print('Area of Rectangle is: ', rect.getArea())
    elif shape == 'Circle':
        cirl = Circle(int(components[1]))
        print('Area of the Circle is: ', cirl.getArea())
    elif shape == 'Triangle':
        tri = Triangle(int(components[1]), int(components[2]))
        print('Area of Triangle is: ', tri.getArea())
    else:
        pass