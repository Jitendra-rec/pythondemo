class student:
    def study(self):
        print('IN student class')
        print('depends on teachers\n')
class programer(student):
    def study(self):
        print('In programer class')
        print('for developing new skilss')
c=programer()
c.study()
