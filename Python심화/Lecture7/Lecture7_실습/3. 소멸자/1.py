# 객체과 파괴될 때 호출됨
# 파라미터를 따로 받지 않는다
# 파이썬에서는 이게 권장하지 않는다



class Courier(object):
    pass

    # def __del__(self):
    #     self.parcels.clear()

A = Courier()
B = A
print(A is B) # A와 B의 메모리가 같다

# 위랑
A = Courier()
B = Courier()
print(A is B)

# --------------
A = Courier()
B = A

del A # 객체의 '이름'을 없앤다. 객체를 명시적으로 없애지 않는다
del A, B # 이렇게 해야 메모리 할당이 해제가 됨
print(id(B))