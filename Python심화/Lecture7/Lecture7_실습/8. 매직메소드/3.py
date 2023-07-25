class DoubleMapper:
    def __init__(self):
        self.mapping = {}

    def __getitem__(self, index):
        return self.mapping.get(index, index * 2)
    
    def __setitem__(self, index, value):
        self.mapping[index] = value

mapper = DoubleMapper()
print(mapper[1, 2])   # testtest
mapper[1, 2] = "설정됨"
print(mapper[1, 2], mapper[2, 4])   # 설정됨

# a[3] = 6
# a["test"] = "testtest"
# a[10] = 10
# a[10] --> 10