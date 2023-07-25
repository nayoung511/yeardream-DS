# __function__ <- 특별한 기능
# 스스로 정의하지 말자! 파이썬에서 내부적으로 구현되어 있음

# 1. 
class Courier:
    #객체가 처음 생성될 때 만들고 호출되는 메소드
    def __init__(self):
        print("생성되었습니다.")

kim = Courier()

# 2.
class Courier:
    def __init__(self, data):
        print(data)

kim = Courier("test")

# 3.
class Courier:
    def __init__(self, data):
        self.data = data
        self.data_lost = "sad"

# 생성자가 attribute를 다 사전에 정의해서 집어 넣어야 한다
kim = Courier("test")
lee = Courier("python")

print(kim.data, lee.data)