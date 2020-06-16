class A:
    def f1(self):
        print('class A f1')
    def f2(self):
        print("class A f2")
class B():
    def f3(self):
        print("Class B f3")
    def f4(self):
        print("class B f4")
class C(A,B):
    def f5(self):
        print("Class C f5")

ob1=C()
ob1.f1()
ob1.f2()
ob1.f3()
ob1.f4()
ob1.f5()