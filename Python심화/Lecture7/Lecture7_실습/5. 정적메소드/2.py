class Number():
    @staticmethod
    def echo_1(): # 그냥 number가 할 수 있는 메소드 중 하나가 되는 것 (self 필요 x)
        print(1)

    def print(self):
        print(self.data)

a = Number()
#a.print(args) # --> Number.print(a, args)
Number.echo_1()
a.echo_1()