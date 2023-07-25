class Integer:
    def __init__(self, data: int):
        self.set_data(data)

    def get_data(self):
        return self._data
    
    def set_data(self, data:int):
        if not isinstance(data, int):
            raise ValueError() 
        self._data = data
    

a = Integer(10)
print(a.get_data())
a.set_data(11)
print(a.get_data())
a.set_data(10.1)
b = Integer(10.1)
