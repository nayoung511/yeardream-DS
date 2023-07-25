# 다른 클래스에게 객체의 내부 감추기

class Courier:
    def __init__(self):
        self.public_data = 1
        self._protected_data = 2
        self.__private_data = 3 # --> self._Courier_private_data

class JejuCourier(Courier):
    def __init__(self):
        super().__init__()
        print(self.public_data)
        print(self.__protected_data)
        print(self.__private_data) # --> self._JejuCourier__private_data

JejuCourier()
#print(a.__private_data) # 실제로는 mangling이 작동된다