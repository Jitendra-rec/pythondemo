class fun:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __add__(self, other):
        print(self.a + other.a,end=' and ')
        print(self.b + other.b)

    def __sub__(self, other):
        print(self.a - other.a, end=' and ')
        print(self.b - other.b)

    def __mul__(self, other):
        print(self.a * other.a, end=' and ')
        print(self.b * other.b)

    def __truediv__(self, other):
        print(self.a / other.a ,end=' and ')
        print(self.b / other.b)

    def __mod__(self, other):
        print(self.a % other.a,end=' end ')
        print(self.b % other.b)

    def __gt__(self, other):
        if self.a > other.a:
            print(self.a,'greater than ',other.a)
        else:
            print(self.a, 'lesser than ', other.a)
        if self.b > other.b:
            print(self.b,'greater than ',other.b)
        else:
            print(self.b, 'lesser than ', other.b)


a1=fun(25,100)
a2=fun(5,12)
a1+a2
a1-a2
a1*a2
a1/a2
a1%a2
a1>a2
