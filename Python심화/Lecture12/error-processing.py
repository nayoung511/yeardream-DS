for i in range (5, -5, -1):
    print("Steps2")
    try:
        value /= i

    except NameError:
        print("Value가 없어서 10으로 지정함")
        value = 10

    except ZeroDivisionError:
        print("0으로 나눔, 넘어감")

    # 모든 클래스의 부모 클래스니까 모든 예외를 잡음
    except Exception as e:
        print(type(e), e)
    
    else:
        print(value)

    finally:
        print("Steps")