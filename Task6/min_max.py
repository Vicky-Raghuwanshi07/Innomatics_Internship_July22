import numpy

N,M = map(int,input().split())
arr = numpy.array([list(map(int,input().split())) for _ in range(int(N))])
mini = numpy.min(arr,axis=1)
maxi= numpy.max(mini)
print(maxi)