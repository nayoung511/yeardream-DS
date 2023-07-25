class Number:
    def __init__(self, data: int):
        self.data = data

    @staticmethod
    def add(a, b):
        return Number(a.data + b.data)

kim = Number(1)
lee = Number(2)
print(Number.add(kim, lee).data)
