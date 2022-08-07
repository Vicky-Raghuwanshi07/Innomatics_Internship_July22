import numpy as np

n,m = map(int, input().split())
l=[]
for i in range(n):
    a = list(map(int, input().split()))
    l.append(a)
l = np.array(l)
s = np.sum(l, axis=0)
print(np.prod(s))


