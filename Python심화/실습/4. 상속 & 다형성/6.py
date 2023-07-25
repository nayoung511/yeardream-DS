class Courier:
    def __init__(self, name):
        self.name = name

    def deliver(self):
        print("배달 중")

class JejuCourier(Courier):
    def __init__(self, name, ticket):
        super().__init__(name)
        self.ticket = ticket

    def deliver(self):
        print(self.ticket, "사용해서 제주도로 이동") # self안에 있는 ticket
        super().deliver()

class OverseasCourier(Courier):
    def __init__(self, name, passport):
        super().__init__(name)
        self.passport = passport

    def deliver(self):
        print(self.passport, "해외로 가는 중")
        super().deliver()

kim = JejuCourier("길동", "비행기표")
park = OverseasCourier("철수", "여권")

super(JejuCourier, kim).deliver()
def 배달하기(courier: Courier):
    courier.deliver()

배달하기(kim)
배달하기(park)
