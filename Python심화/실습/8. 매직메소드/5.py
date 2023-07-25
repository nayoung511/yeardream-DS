class Dataset:
    def __init__(self, data, times=3):
        self.data = data
        self.times = times

    def __len__(self):
        return len(self.data) * self.times
    
    def __getitem__(self, index):
        if index >= len(self):
            raise IndexError()
        
        # 10의 인덱스는 0, 4, 8, 12 ...
        return self.data[index % len(self.data)]
    
dataset = Dataset([10, 2, 5, 2], times=5)
print(len(dataset))
print(dataset[12])

for item in dataset:
    print(item)

"""
for 문을 돌 수 있는 이유가 매직 메소드를 사용했기 때문임
"""