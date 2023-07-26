import pickle

class Complex:
    def __init__(self, real: float, img: float):
        self.real = real
        self.img = img

    def __str__(self):
        return f"{self.real:.3f}+{self.img:.3f}j"
    
    def __add__(self, other):
        return Complex(
            self.real + other.real, 
            self.img + other.img
        )
    
a = Complex(1.2, 3.3)

with open("test_int.pkl", "wb") as fd:
    pickle.dump(a, fd)

"""
정의된 대상에 대해서만 피클을 사용할 수 있다
"""