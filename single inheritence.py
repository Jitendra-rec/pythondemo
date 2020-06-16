class A:
    def f1(self):
        print('class A f1')
    def f2(self):
        print("class A f2")
class B(A):
    def f3(self):
        print("Class B f3")
    def f4(self):
        print("class B f4")

ob1=B()
ob1.f1()
ob1.f2()
ob1.f3()
ob1.f4()