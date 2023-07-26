for i in range (-5, 5):
    try:
        print(f"{i}로 뭔가 하는 중 ...")
        print(10 / i)
        print(f"{i}로 뭔가 마무리 중 ...")
    except ZeroDivisionError:
        print("0 나누기 에러가 발생함 무시하고 진행")