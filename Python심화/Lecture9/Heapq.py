import heapq

a = [3, 5, 1, 7, 6]
# O(N^2)
print(sorted(a)[-1])
# 입력이 계속 된다고 했을 때 이렇게 되면 많이 느려짐

queue = [5, 2, 7, 4, 1, 10, 9, 8] # O(N log N)
heapq.heapify(queue) # 개념적으로 트리구조가 된다
print(queue)    # [1, 2, 7, 4, 5, 10, 9, 8]
print(queue[0]) # 1

# heappush O(log N)
heapq.heappush(queue, 11) 
heapq.heappush(queue, -2)
heapq.heappush(queue, 3)
print(queue)
# [-2, 1, 7, 4, 2, 10, 9, 8, 11, 5, 3]
print(queue)

#heappop
print(heapq.heappop(queue))
print(queue)
print(heapq.heappop(queue))
print(queue)