class Courier:
    Nationality = "KOR"

Kim = Courier() # Courier 객체를 만들어서 a에 담아줌
Lee = Courier()

print(Courier.Nationality)
print(Kim.Nationality)
print(Lee.Nationality)

Courier.Nationality = "US"

print(Courier.Nationality)
print(Kim.Nationality)
print(Lee.Nationality)


#print(a is b) # FALSE 두 개는 다른 객체
# 전역변수를 추천하지 않는다