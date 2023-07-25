class 동물:
    def 밥먹기(self):
        print("냠냠")

    def 잠자기(self):
        print("zzzz")

class 나는것(동물):
    def 잠자기(self):
        print("땅에 내려가서 자는 중")
        super().잠자기() # --> super(나는것)

# super() 부모의 클래스를 자기 자신에게 넣어서 실행시키겠다
batman = 나는것()
batman.잠자기()

"""
땅에 내려가서 자는 중
zzzz
"""