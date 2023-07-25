# __call__
# 객체를 함수처럼 사용하고 싶다
class AdditionNumber:
    def __init__(self, addition:int):
        self.addition = addition

    def __call__(self, number:int):
        return self.addition + number
    
    def __call__(self, number:int):
        return self.addition - number

add_5 = AdditionNumber(5)
add_10 = AdditionNumber(10)

print(add_5(7), add_10(7))