import numpy

n,m = map(int, input().split())
a,b = [],[]
for i in range(n):
    l1 = list(map(int, input().split()))
    a.append(l1)
for i in range(n):
    l2 = list(map(int, input().split()))
    b.append(l2)
a = numpy.array(a, int)
b = numpy.array(b, int)
print(numpy.add(a,b))
print(numpy.subtract(a,b))
print(numpy.multiply(a,b))
print(a//b)
print(numpy.mod(a,b))
print(numpy.power(a,b))
