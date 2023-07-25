class 한국거주:
    def 서울가기(self):
        print("서울로 가는 중")

class 동물:
    def 밥먹기(self):
        print("냠냠")

    def 잠자기(self):
        print("zzzz")

    def 울기(self):
        print("와아아아아아")


class 고양이(동물, 한국거주):
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

sori = 고양이()
sori.울기()
sori.서울가기()