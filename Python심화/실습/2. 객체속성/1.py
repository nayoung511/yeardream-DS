class Courier:
    pass

kim = Courier()
lee = Courier()

kim.data = 1
lee.data2 = 2

print(kim.data)
print(lee.data2)
# 같은 클래스 안에서 두 객체가 다른 attribute를 가지게 된다
# --> 객체 지향을 위반
# OOP에서는 attribute를 각각 mapping해서 넣기를 원했는데 이게 안됨

#print(kim.data2) #에러발생


# 어떻게 해결하면 좋을까?
# --> 생성할 때 모두가 같은 [초기화 과정]