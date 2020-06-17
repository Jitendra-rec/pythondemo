class student:
    def study(self):
        print('IN student class')
        print('depends on teachers\n')
class programer:
    def study(self):
        print('In programer class')
        print('for developing new skilss')

class teacher:
    def getup(self,g):
        g.study()

l1=student()
l2=programer()
teah=teacher()
teah.getup(l1)
teah.getup(l2)
