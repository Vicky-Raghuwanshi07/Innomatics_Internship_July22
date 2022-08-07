import numpy
n = int(input())
l=[]
for i in range(n):
    a = list(map(float, input().split()))
    l.append(a)
print(round(numpy.linalg.det(l),2))

