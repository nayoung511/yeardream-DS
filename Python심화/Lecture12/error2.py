try:
    while True:
        value = input("A B C 중 하나를 입력해주세요: ")

        if len(value) == 1 and value not in "ABC":
            raise ValueError("잘못된 입력")
        
        print("선택된 옵션", value)
except ValueError as e:
    print(e)