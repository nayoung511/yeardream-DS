# 자원을 획득하고 사용 후 반납해야 하는 경우 주로 사용합니다.
# 1) 자원을 획득한다
# 2) 자원을 사용한다
# 3) 자원을 반납한다

class Hello:
    def __enter__(self):
        # 사용할 자원을 가져오거나 만든다(핸들러 등)
        print('enter...')
        return self # 반환값이 있어야 VARIABLE를 블록내에서 사용할 수 있다
        
    def sayHello(self, name):
        # 자원을 사용한다. ex) 인사한다
        print('hello ' + name)

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 마지막 처리를 한다(자원반납 등)
        print('exit...')

with Hello() as h:
    h.sayHello('obama')
    h.sayHello('trump')