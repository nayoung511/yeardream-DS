from collections import namedtuple

Coords3D = namedtuple("Coords3D", ['x', 'y', 'z'])
point = Coords3D(10, 20, z=30)
print(point.x, point.y)
print(point[0], point[1])

print(*point)
