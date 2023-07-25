class Number():
    @staticmethod
    def number_factory(data):
        obj = Number()
        obj.value = data
        return obj
    
    @staticmethod
    def complex_factor(real:int, fake:int):
        obj = Number()
        obj.value = complex(real, fake)
        return obj
    
a = Number.number_factory(1)
b = Number.complex_factor(3, 4)
print(type(a))
print(a.value) 

"""
장점: 생성자를 여러개 만들 수 있다.
number_factory 용 생성자, complex_factor 용 생성자 하나
"""