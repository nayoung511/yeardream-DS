from collections import Counter

# counter initialize
c = Counter({"a":5, "b":3})
print(c)
print(c.keys())
print(c.items())
print(list(c.elements()))

c = Counter(a=5, b=3) # 이렇게도 선언 가능
print(c)

a = Counter([1, 1, 2, 2, 2, 3])
b = Counter([2, 3, 3, 4])

print(a, b)

print(a + b) # 합치기
print(a & b) # 교집합