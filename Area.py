# task 01: wap tp calculate the area and perimeter of a rectangle
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculatearea(self):
        Area = self.length * self.width
        return Area
        

    def calculateperimeter(self):
        perimeter= 2 * (self.length + self.width)
        return perimeter


length = float(input("Enter the length : "))
width = float(input("Enter the Width : "))
rectangle = Rectangle(length, width)
area = rectangle.calculatearea()
perimeter = rectangle.calculateperimeter()
print(f"Area of the rectangle: {area}")
print(f"Perimeter of the rectangle: {perimeter}")


