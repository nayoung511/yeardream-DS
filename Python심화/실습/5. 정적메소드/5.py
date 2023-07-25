class Real:
    def __init__(self, data: int):
        self.data = data

    @classmethod #클래스 인스턴스가 아닌 클래스 자체가 넘어오게 됩니다
    def add(cls, a, b):
        return cls(a.data + b.data)

class Integer(Real):
    def __init__(self, data):
        self.data = data


kim = Integer(1)
lee = Integer(2)
#print(type(Integer.add(kim, lee))) # --> cls 없이는Real이 나옴

Integer.add(kim, lee)
Real.add(kim, lee)