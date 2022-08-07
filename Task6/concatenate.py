import numpy

n,m,p = map(int, input().split())
arr1,arr2 = [],[] 
for i in range(n):
    l1 = list(map(int, input().split()))
    arr1.append(l1)
for j in range(m):
    l2 = list(map(int, input().split()))
    arr2.append(l2)
a = numpy.array(arr1)
b = numpy.array(arr2)
print(numpy.concatenate((a,b)))


