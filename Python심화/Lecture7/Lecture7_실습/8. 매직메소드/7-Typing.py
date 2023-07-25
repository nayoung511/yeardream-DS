class Courier:
    def __init__(self, name:str, address:str):
        self.name = name
        self.address = address

    def __lt__(self, other):
        return self.name < other.name
    
    def __lt__(self, other):
        return self.address < other.address

    def __str__(self):
        return self.address + ' 담당 ' + self.name

a = Courier("김기사", "판교")
b = Courier("박기사", "성북구")
c = Courier("이기사", "가")
d = Courier("최기사", "나")

# 문자 길이에 상관없이 가나다 순으로 비교
print(a < b) # False
print(c < d) # True

courier_list = [
    Courier("김기사", "판교"),
    Courier("박기사", "성북구"),
    Courier("이기사", "가"),
    Courier("최기사", "나")
]

print(courier_list)
for courier in sorted(courier_list): # address 기준으로 sorted
    print(courier.name)