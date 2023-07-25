a: str = "TB"
"""
가독성용: 남들에게 이 함수의 파라미터는 어떤 형태가 들어가는 것을 알려주는 것
"""

def print_str(text: str):
    print(text)

print_str("abc") # 실행 ok
print(123) # 실행 ok

def add(a: int, b: int) -> int:
    return a + b

print(add(1, 2))
print(add("test", "abc"))

