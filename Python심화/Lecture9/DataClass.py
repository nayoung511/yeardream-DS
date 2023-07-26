from dataclasses import dataclass

# 데이터를 담기 위한 클래스/ 기능을 하는건 아니야
@dataclass
class Coords3D:
    x: float
    y: float
    z: float = 0

    def norm(self) -> float:
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
    

coord1 = Coords3D(x = 1, y = 2, z = 3)
coord2 = Coords3D(x = 4, y = 5, z = 6)