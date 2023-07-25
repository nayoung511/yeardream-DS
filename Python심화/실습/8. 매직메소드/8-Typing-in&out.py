class Complex:
    def __init__(self, real: float, img: float):
        self.real = real
        self.img = img

    def __str__(self):
        return str(self.real) + "+" + str(self.img) + "j"
    
    def __add__(self, other):
        return Complex(self.real + other.real, self.img + other.img)
    
    def __sub__(self, other):
        return Complex(self.real - other.real, self.img - other.img)
    
    # inplace 연산
    def __iadd__(self, other):
        self.real += other.real
        self.img += other.img
    
a = Complex(1.2, 3.6)
b = Complex(1.2, -5.7)
#print(a - b)

a = Complex(1, 2)
b = Complex(2, 1)

print(a, id(a))
a = a + b
print(a, id(a))
print(type(a), type(b))
a += b
print(a, id(a))

"""
a = a + b (outplace 연산)
a += b (inplace 연산)
서로 다르다

a + b 라는 연산으로 새로운 객체가 나온거다. 그게 a로 지칭하는 것 뿐

"""