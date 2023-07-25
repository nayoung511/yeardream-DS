class DoubleMapper:
    def __init__(self):
        self.mapping = {}

    def get(self, index):
        return self.mapping.get(index, index * 2)
    
    def set(self, index, value):
        self.mapping[index] = value

mapper = DoubleMapper()
print(mapper.get("test"))   # testtest
mapper.set("test", "설정됨")
print(mapper.get("test"))   # 설정됨

# a[3] = 6
# a["test"] = "testtest"
# a[10] = 10
# a[10] --> 10