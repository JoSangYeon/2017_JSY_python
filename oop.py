class Shape:
    def getArea(self):
        pass

class Triangle(Shape):
    def __init__(self,width, height):
        self.width = width
        self.height = height
    def getArea(self):
        area = self.width * self.height / 2.0
        return area

class Square(Shape):
    def __init__(self,size):
        self.size = size
    def getArea(self):
        area = size**2
        return area

def PrintArea(Shape):
    if Shape.isinstance(Shape):
        a = Shape.getArea()
    print(a)


aaa = Triangle(5,3)
bbb = Square(4)


PrintArea(aaa)

PrintArea(bbb)
