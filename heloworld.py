from numpy import*
a=array([],'i')
n=int(input('enter the size of array '))
for i in range(n):
    a=append(a,int(input()))
    a.sort()
print(a)
