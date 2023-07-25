# 다른 클래스에게 객체의 내부 감추기
# 캡슐화, 정보 은닉
# 클래스 간 간섭 최소화
# 최소한의 정보만을 지정된 API로 공개

class Courier:
    def __init__(self):
        self.public_data = 1
        self.__private_data = 2 
        # private 변수 / 함수 이름 앞에 __를 붙임
        # 변수를 내부적으로 사용할거야 (__ 2번)
        # private - 나 자신의 class
        # protected - 나 자신의 클래스랑 내 자식 클래스들 (_ 한번)
        # public - 아무나 접근 가능


a = Courier()
print(a.public_data)
print(a.__private_data)

# class Client:
#     def __init__(self):
#         self.data2

#     def method(self, courier:Courier):
#         courier.data = 2
