class MyError(Exception):
    def __init__(self, value):
        self.value = value
    
try:
    print("뭔가 하는 중")
    raise MyError(6)
except MyError as exception:
    print(exception.value)