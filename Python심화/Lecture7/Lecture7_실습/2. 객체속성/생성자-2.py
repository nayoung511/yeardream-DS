class Courier:
    def __init__(self, name: str):
        self.name = name
        # self.data = None # 밖에서 이름을 만들지 말고 쓸거라면 명시해주자
        self.parcels = []

    def assign(self, parcel: str) -> None:
        self.parcels.append(parcel)

    def deliver(self) -> None:
        for parcel in self.parcels:
            print(self.name, parcel, "배달 중")


kim = Courier("김기사")
lee = Courier("이기사")

kim.assign("TV")
kim.assign("iPhone")

lee.assign("노트북")

kim.deliver()
lee.deliver()

lee.name = "Test"
lee.deliver()
