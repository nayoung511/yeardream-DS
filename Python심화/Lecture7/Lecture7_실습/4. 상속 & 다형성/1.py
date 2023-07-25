# 기존에 구현틀 상속 -> 새로운 틀 제작

class 동물:
    def 밥먹기(self):
        print("냠냠")

    def 잠자기(self):
        print("zzzz")

me = 동물()
me.밥먹기()

class 고양이(동물):
    def 울기(self):
        print("미야용")

class 개(동물):
    def 주인님찾기(self):
        print("사랑해요")

class 말(동물):
    def 누군가태우기(self, human):
        print(human, "태우기")

sori = 고양이()
felix = 개()
epona = 말()

felix.밥먹기()
sori.밥먹기()
epona.밥먹기()



