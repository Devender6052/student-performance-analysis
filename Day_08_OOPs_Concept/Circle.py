class Circle:
    def __init__(self,radius):
        self.radius=radius
        print("Circle of radius",radius,"Created successfully")

    def Area(self):
        print("Area of the circle is ",3.14*self.radius*self.radius)

    def Perimeter(self):
        print("Perimeter of the circle is ",3.14*self.radius*2)

circle1=Circle(5)
circle1.Area()
circle1.Perimeter()