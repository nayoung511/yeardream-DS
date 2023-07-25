# 같은 이름의 메소드를 다르게 작성
# 각 자식 클래스가 다른 클래스와 차별
# 내가 울기라는 메소드가 있는지 확인하고, 없으면 부모가서 확인!!

class 동물:
    def 밥먹기(self):
        print("냠냠")

    def 잠자기(self):
        print("zzzz")

    def 울기(self):
        print("와아아아아아")

class 고양이(동물):
    def 뒹굴거리기(self):
        print("골골골골")

    def 울기(self):
        print("야요옹")

class 개(동물):
    def 주인님찾기(self):
        print("사랑해요")
    def 울기(self):
        print("멍멍")

class 말(동물):
    def 누군가태우기(self, human):
        print(human, "태우기")
    def 울기(self):
        print("히이잉")

me = 동물()
sori = 고양이()
felix = 개()
epona = 말()

# me.울기()
# felix.울기()
# sori.울기()
# epona.울기()


# 다형성 없으면 이렇게 해야됨

    # if isinstance(animal, 고양이):
    #     animal.고양이_울기()


def 울어보기(animal: 동물):
    animal.울기()

울어보기(me)
울어보기(sori)
울어보기(felix)
