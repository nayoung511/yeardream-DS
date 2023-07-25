class 동물:
    def 밥먹기(self):
        print("냠냠")

    def 잠자기(self):
        print("zzzz")

class 포유류(동물):
    def 잠자기(self):
        print("포유류 자는 중")

class 나는것(동물):
    def 잠자기(self):
        print("땅에 내려가서 자는 중")

class 박쥐(포유류, 나는것):
    pass

print(박쥐.mro())
# [<class '__main__.박쥐'>, 
#  <class '__main__.포유류'>, 
#  <class '__main__.나는것'>, 
#  <class '__main__.동물'>, 
#  <class 'object'>]

batman = 박쥐()

박쥐().잠자기() # 박쥐에 잠자기가 없네? 그럼 포유류 먼저니까 포유류 잠자기 프린트 먼저 해야겠네s
batman.잠자기() # 포유류먼저? 아니면 나는것먼저?

"""
# mro(Method resolution order):
    - 실행되는 순서
"""