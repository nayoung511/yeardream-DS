class Coords3D:
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @property
    def z(self):
        return self._z
    

coord1 = Coords3D(x = 1, y = 2, z = 3)
coord2 = Coords3D(x = 4, y = 5, z = 6)

"""
가독성 측면에서는 
coord1 = (1, 2, 3)
coord2 = (4, 5, 6) 보다 낫지만 너무 귀찮다!
"""