class Courier:
    def 택배전달(self,parcel1):
        return id(self)

kim = Courier()
kim.택배전달("TV")
# print(id(kim))
# print(kim.return_id())
#kim.return_id() # --> Courier.택배전달(kim)