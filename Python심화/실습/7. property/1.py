class Circle:
    PI = 3.141592

    def __init__(self, radius: float=3.):
        self.radius = radius

    def get_area(self):
        return Circle.PI * self.radius **2
    
    def set_area(self, value):
        self.radius = (value / Circle.PI) ** .5
a = Circle(5.)
print(a.get_area())
a.set_area(50)
print(a.radius)
print(a.get_area())

# pythonic 하지 않다!