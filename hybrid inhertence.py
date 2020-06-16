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
class C(A):
    def f5(self):
        print("Class C f5")
class D(B):
    def f6(self):
        print("Class D f6")

ob1=D()
ob2=B()
ob1.f1()
ob1.f2()
ob1.f6()
ob2.f1()
ob2.f2()
ob1.f5()