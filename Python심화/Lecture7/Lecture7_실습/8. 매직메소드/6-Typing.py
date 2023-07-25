class Courier:
    def __init__(self, name:str, address:str):
        self.name = name
        self.address = address

    def __str__(self):
        return self.address + ' 담당 ' + self.name

print(str(Courier("김기사", "판교")))
print(type(str(Courier("김기사", "판교")))) # string
