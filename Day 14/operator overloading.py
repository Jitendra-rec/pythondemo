class student:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __add__(self, other):
        m=self.a+other.a
        n=self.b+other.b
        a=student(m,n)
        return a
    def __sub__(self, other):
        m=self.a-other.a
        n=self.b-other.b
        print('the subtraction is',m,n)
s1=student(5,10)
s2=student(2,4)
s3=s1+s2
print(s3.a)
s1-s2
