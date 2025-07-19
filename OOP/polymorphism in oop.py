
class Shape:
    pass

class Circle():
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        print("the area of circle is:",(self.radius**2)*3.14)


class Recatangle():
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth


    def area(self):
        print("the area of the rectangle",self.length*self.breadth)
        

if __name__=="__main__":
    obj1=Circle(2)
    obj1.area()
    obj2=Recatangle(1,2)
    obj2.area()
