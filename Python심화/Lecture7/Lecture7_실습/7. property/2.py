# 메소드지만 마치 attribute처럼 활용할 수 있다.

class Circle:
    PI = 3.141592

    def __init__(self, radius: float=3.):
        self.radius = radius

    @property
    def area(self):
        return Circle.PI * self.radius ** 2

    @area.setter
    def area(self,value):
        self.radius = (value / Circle.PI) ** .5
        
a = Circle(5.)
a.area = 5
print(a.radius)
