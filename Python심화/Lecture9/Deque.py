from collections import deque

queue = deque()
print(queue)
queue = deque([10, 5, 12])
print(queue)

# 앞에 넣기
queue.appendleft(1)
print(queue)

# 뒤에 넣기
queue.append(20)
print(queue)

# 이거랑 동일
array = [10, 5, 12]
array.insert(0, 16)
print(array)

# popleft - 앞 삭제
queue = deque([1, 10, 5, 12, 20])
queue.popleft()
print(queue)

# pop - 뒤 삭제
queue = deque([1, 10, 5, 12, 20])
queue.pop()
print(queue)