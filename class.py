class Rectangle:
    def getArea(self, length, width):
        print(length * width)
    
    def getPerimeter(self, length, width):
        print(2 * (length + width))

obj1 = Rectangle()
obj1.getArea(5, 6)
obj1.getPerimeter(5, 6)
